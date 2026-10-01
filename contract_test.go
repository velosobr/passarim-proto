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

// O serviço precisa expor exatamente os três métodos que o BFF usa.
func TestCatalogServiceMethods(t *testing.T) {
	sd := catalogv1.File_passarim_catalog_v1_catalog_proto.Services().ByName("CatalogService")
	if sd == nil {
		t.Fatal("CatalogService não encontrado no descriptor")
	}
	want := []string{"ListSpecies", "GetSpecies", "ListFilters"}
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
