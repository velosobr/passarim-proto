// Testes de contrato: garantem que o código gerado a partir do .proto
// se comporta como os serviços (catalog e BFF) esperam.
// Se alguém mudar o .proto de um jeito que quebre essas garantias,
// o teste falha antes de o problema chegar em produção.
package passarimproto_test

import (
	"testing"

	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protoreflect"

	catalogv1 "github.com/velosobr/passarim-proto/gen/go/passarim/catalog/v1"
	curatorv1 "github.com/velosobr/passarim-proto/gen/go/passarim/curator/v1"
)

// Uma espécie completa deve sobreviver a ida e volta pelo formato binário
// (é exatamente o que acontece quando ela trafega via gRPC).
func TestSpeciesRoundTrip(t *testing.T) {
	size := int32(100)
	diet := "Sementes de palmeiras"
	original := &catalogv1.Species{
		Id:                 "anodorhynchus-hyacinthinus",
		ScientificName:     "Anodorhynchus hyacinthinus",
		CommonNamePt:       "Arara-azul",
		Family:             "Psittacidae",
		SizeCm:             &size,
		Diet:               &diet,
		ConservationStatus: catalogv1.ConservationStatus_CONSERVATION_STATUS_VU,
		Description:        "Maior psitacídeo do mundo.",
		DescriptionCredit: &catalogv1.Credit{
			Author: "Equipe Passarim", License: "CC-BY-SA", Source: "curated",
		},
		Facts:   []*catalogv1.Fact{{Text: "Quebra cocos com o bico.", Source: "curated"}},
		Biomes:  []catalogv1.Biome{catalogv1.Biome_BIOME_PANTANAL, catalogv1.Biome_BIOME_CERRADO},
		States:  []string{"MS", "MT"},
		Photos: []*catalogv1.Photo{{
			ThumbKey: "species/abc/p1-thumb.webp", MediumKey: "species/abc/p1-medium.webp",
			LargeKey: "species/abc/p1-large.webp", Width: 1600, Height: 1067,
			Credit: &catalogv1.Credit{Author: "Fulano", License: "CC-BY-NC", Source: "inaturalist", SourceUrl: "https://www.inaturalist.org/photos/1"},
		}},
		Audio: &catalogv1.Audio{
			Key: "species/abc/a1.m4a", DurationMs: 12000,
			Credit: &catalogv1.Credit{Author: "Beltrano", License: "CC-BY-NC-SA", Source: "xeno-canto", SourceUrl: "https://xeno-canto.org/1"},
		},
		Clusters: []*catalogv1.OccurrenceCluster{{Lat: -19.0, Lng: -57.6, Count: 42}},
	}

	bytes, err := proto.Marshal(original)
	if err != nil {
		t.Fatalf("marshal: %v", err)
	}
	decoded := &catalogv1.Species{}
	if err := proto.Unmarshal(bytes, decoded); err != nil {
		t.Fatalf("unmarshal: %v", err)
	}
	if !proto.Equal(original, decoded) {
		t.Fatalf("espécie mudou na ida e volta:\nantes:  %v\ndepois: %v", original, decoded)
	}
}

// Review Focus #1: "ausente" precisa ser diferente de "zero".
// Uma ave sem canto não pode virar um canto vazio de duração 0;
// uma ave de tamanho desconhecido não pode virar "0 cm".
func TestSpeciesOptionalFieldsPresence(t *testing.T) {
	s := &catalogv1.Species{Id: "x"}
	bytes, _ := proto.Marshal(s)
	decoded := &catalogv1.Species{}
	if err := proto.Unmarshal(bytes, decoded); err != nil {
		t.Fatalf("unmarshal: %v", err)
	}
	if decoded.Audio != nil {
		t.Error("Audio deveria ser nil quando a ave não tem canto")
	}
	if decoded.SizeCm != nil {
		t.Error("SizeCm deveria ser nil quando o tamanho é desconhecido")
	}
	if decoded.Diet != nil {
		t.Error("Diet deveria ser nil quando a dieta é desconhecida")
	}
}

// Review Focus #2: se uma versão futura do catalog mandar um bioma novo
// (ex.: valor 99), um BFF antigo não pode falhar ao ler a mensagem.
// Em proto3 os enums são "abertos": o número desconhecido é preservado.
func TestUnknownEnumValueSurvivesRoundTrip(t *testing.T) {
	s := &catalogv1.Species{Id: "x", Biomes: []catalogv1.Biome{catalogv1.Biome(99)}}
	bytes, _ := proto.Marshal(s)
	decoded := &catalogv1.Species{}
	if err := proto.Unmarshal(bytes, decoded); err != nil {
		t.Fatalf("enum desconhecido quebrou o unmarshal: %v", err)
	}
	if len(decoded.Biomes) != 1 || decoded.Biomes[0] != catalogv1.Biome(99) {
		t.Fatalf("valor desconhecido não foi preservado: %v", decoded.Biomes)
	}
}

// O serviço precisa expor exatamente os quatro métodos que o BFF usa (o
// GetFeaturedSpecies, a "Ave do dia", veio na frente B).
func TestCatalogServiceMethods(t *testing.T) {
	sd := catalogv1.File_passarim_catalog_v1_catalog_proto.Services().ByName("CatalogService")
	if sd == nil {
		t.Fatal("CatalogService não encontrado no descriptor")
	}
	want := []string{"ListSpecies", "GetSpecies", "ListFilters", "GetFeaturedSpecies"}
	if sd.Methods().Len() != len(want) {
		t.Fatalf("esperava %d métodos, veio %d", len(want), sd.Methods().Len())
	}
	for _, name := range want {
		if sd.Methods().ByName(protoreflect.Name(name)) == nil {
			t.Errorf("método %s ausente", name)
		}
	}
}

// O mapa usa a precisão (em graus) para desenhar o raio de cada cluster.
func TestOccurrenceClusterHasPrecision(t *testing.T) {
	c := &catalogv1.OccurrenceCluster{Lat: -19, Lng: -57, Count: 3, Precision: 0.5}
	bytes, _ := proto.Marshal(c)
	decoded := &catalogv1.OccurrenceCluster{}
	if err := proto.Unmarshal(bytes, decoded); err != nil {
		t.Fatalf("unmarshal: %v", err)
	}
	if decoded.GetPrecision() != 0.5 {
		t.Fatalf("precision = %v, want 0.5", decoded.GetPrecision())
	}
}

// O veredito do curador precisa sobreviver à ida e volta pelo formato binário,
// porque é assim que ele viaja do curador (Python) até o worker (Go) via gRPC.
func TestPhotoVerdictRoundTrip(t *testing.T) {
	original := &curatorv1.ClassifyPhotosResponse{
		ModelVersion: "rtdetr-r50vd+openclip-b32@1",
		Verdicts: []*curatorv1.PhotoVerdict{{
			PhotoId:         "144156085",
			Category:        curatorv1.PhotoCategory_PHOTO_CATEGORY_SINGLE_BIRD,
			BirdCount:       1,
			LargestBirdArea: 0.8,
			LargestBirdCut:  true,
			Sharpness:       0.6,
			Confidence:      0.9,
		}},
	}
	data, err := proto.Marshal(original)
	if err != nil {
		t.Fatalf("marshal: %v", err)
	}
	var got curatorv1.ClassifyPhotosResponse
	if err := proto.Unmarshal(data, &got); err != nil {
		t.Fatalf("unmarshal: %v", err)
	}
	if !proto.Equal(original, &got) {
		t.Fatalf("ida e volta mudou a mensagem:\n antes %v\n depois %v", original, &got)
	}
}

// Os números do enum são parte do contrato: o worker grava a categoria no banco
// e o curador a envia como número. Trocar um número mudaria o significado de
// fotos já classificadas, então o teste trava cada um.
func TestPhotoCategoryNumbersAreStable(t *testing.T) {
	want := map[curatorv1.PhotoCategory]protoreflect.EnumNumber{
		curatorv1.PhotoCategory_PHOTO_CATEGORY_UNSPECIFIED: 0,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_SINGLE_BIRD: 1,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_FLOCK:       2,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_NEST:        3,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_EGGS:        4,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_FEATHER:     5,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_DEAD_BIRD:   6,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_NO_BIRD:     7,
		curatorv1.PhotoCategory_PHOTO_CATEGORY_OTHER:       8,
	}
	for category, number := range want {
		if category.Number() != number {
			t.Errorf("%v: número %d, esperado %d", category, category.Number(), number)
		}
	}
	if n := len(curatorv1.PhotoCategory_name); n != len(want) {
		t.Errorf("o enum tem %d valores, o teste conhece %d: atualize o teste e o worker", n, len(want))
	}
}

// Os campos da frente B (conteúdo Kids, bioma principal, picos do canto e a
// "Ave do dia") também sobrevivem à ida e volta pelo formato binário.
func TestKidsAndFeaturedRoundTrip(t *testing.T) {
	species := &catalogv1.Species{
		Id:           "turdus-rufiventris",
		PrimaryBiome: catalogv1.Biome_BIOME_MATA_ATLANTICA,
		Kids: &catalogv1.KidsContent{
			Description: "O sabiá tem a barriga cor de laranja.",
			Facts:       []*catalogv1.KidsFact{{Text: "O canto dele pode durar dois minutos.", SourceFact: 1}},
			DidYouKnow:  "O sabiá imita outras aves.",
		},
		Audio: &catalogv1.Audio{Key: "species/t/a.aac", DurationMs: 3000, Peaks: []float32{0, 0.5, 1}},
	}
	featured := &catalogv1.GetFeaturedSpeciesResponse{
		Species: &catalogv1.SpeciesSummary{Id: "turdus-rufiventris", PrimaryBiome: catalogv1.Biome_BIOME_MATA_ATLANTICA},
		Audio:   &catalogv1.Audio{Key: "species/t/a.aac", Peaks: []float32{1}},
	}
	requests := []proto.Message{
		&catalogv1.ListSpeciesRequest{KidsOnly: true, PrimaryBiome: catalogv1.Biome_BIOME_PAMPA},
		&catalogv1.ListFiltersRequest{KidsOnly: true},
		&catalogv1.ListFiltersResponse{PrimaryBiomeCounts: []*catalogv1.BiomeCount{{Biome: catalogv1.Biome_BIOME_PAMPA, SpeciesCount: 2}}},
		&catalogv1.GetFeaturedSpeciesRequest{Date: "2026-10-28"},
	}
	for _, original := range append([]proto.Message{species, featured}, requests...) {
		bytes, err := proto.Marshal(original)
		if err != nil {
			t.Fatalf("marshal: %v", err)
		}
		decoded := original.ProtoReflect().New().Interface()
		if err := proto.Unmarshal(bytes, decoded); err != nil {
			t.Fatalf("unmarshal: %v", err)
		}
		if !proto.Equal(original, decoded) {
			t.Fatalf("mensagem mudou na ida e volta:\nantes:  %v\ndepois: %v", original, decoded)
		}
	}
}
