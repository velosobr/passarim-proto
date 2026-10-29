from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Biome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BIOME_UNSPECIFIED: _ClassVar[Biome]
    BIOME_AMAZONIA: _ClassVar[Biome]
    BIOME_MATA_ATLANTICA: _ClassVar[Biome]
    BIOME_CERRADO: _ClassVar[Biome]
    BIOME_CAATINGA: _ClassVar[Biome]
    BIOME_PANTANAL: _ClassVar[Biome]
    BIOME_PAMPA: _ClassVar[Biome]

class ConservationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSERVATION_STATUS_UNSPECIFIED: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_LC: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_NT: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_VU: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_EN: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_CR: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_EW: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_EX: _ClassVar[ConservationStatus]
    CONSERVATION_STATUS_DD: _ClassVar[ConservationStatus]
BIOME_UNSPECIFIED: Biome
BIOME_AMAZONIA: Biome
BIOME_MATA_ATLANTICA: Biome
BIOME_CERRADO: Biome
BIOME_CAATINGA: Biome
BIOME_PANTANAL: Biome
BIOME_PAMPA: Biome
CONSERVATION_STATUS_UNSPECIFIED: ConservationStatus
CONSERVATION_STATUS_LC: ConservationStatus
CONSERVATION_STATUS_NT: ConservationStatus
CONSERVATION_STATUS_VU: ConservationStatus
CONSERVATION_STATUS_EN: ConservationStatus
CONSERVATION_STATUS_CR: ConservationStatus
CONSERVATION_STATUS_EW: ConservationStatus
CONSERVATION_STATUS_EX: ConservationStatus
CONSERVATION_STATUS_DD: ConservationStatus

class Credit(_message.Message):
    __slots__ = ("author", "license", "source", "source_url")
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    author: str
    license: str
    source: str
    source_url: str
    def __init__(self, author: _Optional[str] = ..., license: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class Photo(_message.Message):
    __slots__ = ("thumb_key", "medium_key", "large_key", "width", "height", "credit")
    THUMB_KEY_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_KEY_FIELD_NUMBER: _ClassVar[int]
    LARGE_KEY_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    thumb_key: str
    medium_key: str
    large_key: str
    width: int
    height: int
    credit: Credit
    def __init__(self, thumb_key: _Optional[str] = ..., medium_key: _Optional[str] = ..., large_key: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., credit: _Optional[_Union[Credit, _Mapping]] = ...) -> None: ...

class Audio(_message.Message):
    __slots__ = ("key", "duration_ms", "credit", "peaks")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    PEAKS_FIELD_NUMBER: _ClassVar[int]
    key: str
    duration_ms: int
    credit: Credit
    peaks: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, key: _Optional[str] = ..., duration_ms: _Optional[int] = ..., credit: _Optional[_Union[Credit, _Mapping]] = ..., peaks: _Optional[_Iterable[float]] = ...) -> None: ...

class Fact(_message.Message):
    __slots__ = ("text", "source")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    text: str
    source: str
    def __init__(self, text: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class OccurrenceCluster(_message.Message):
    __slots__ = ("lat", "lng", "count", "precision")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lng: float
    count: int
    precision: float
    def __init__(self, lat: _Optional[float] = ..., lng: _Optional[float] = ..., count: _Optional[int] = ..., precision: _Optional[float] = ...) -> None: ...

class SpeciesSummary(_message.Message):
    __slots__ = ("id", "scientific_name", "common_name_pt", "thumbnail_key", "conservation_status", "primary_biome")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCIENTIFIC_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_NAME_PT_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_KEY_FIELD_NUMBER: _ClassVar[int]
    CONSERVATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BIOME_FIELD_NUMBER: _ClassVar[int]
    id: str
    scientific_name: str
    common_name_pt: str
    thumbnail_key: str
    conservation_status: ConservationStatus
    primary_biome: Biome
    def __init__(self, id: _Optional[str] = ..., scientific_name: _Optional[str] = ..., common_name_pt: _Optional[str] = ..., thumbnail_key: _Optional[str] = ..., conservation_status: _Optional[_Union[ConservationStatus, str]] = ..., primary_biome: _Optional[_Union[Biome, str]] = ...) -> None: ...

class Species(_message.Message):
    __slots__ = ("id", "scientific_name", "common_name_pt", "family", "size_cm", "diet", "conservation_status", "description", "description_credit", "facts", "biomes", "states", "photos", "audio", "clusters", "kids", "primary_biome")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCIENTIFIC_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_NAME_PT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    SIZE_CM_FIELD_NUMBER: _ClassVar[int]
    DIET_FIELD_NUMBER: _ClassVar[int]
    CONSERVATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CREDIT_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    BIOMES_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    KIDS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BIOME_FIELD_NUMBER: _ClassVar[int]
    id: str
    scientific_name: str
    common_name_pt: str
    family: str
    size_cm: int
    diet: str
    conservation_status: ConservationStatus
    description: str
    description_credit: Credit
    facts: _containers.RepeatedCompositeFieldContainer[Fact]
    biomes: _containers.RepeatedScalarFieldContainer[Biome]
    states: _containers.RepeatedScalarFieldContainer[str]
    photos: _containers.RepeatedCompositeFieldContainer[Photo]
    audio: Audio
    clusters: _containers.RepeatedCompositeFieldContainer[OccurrenceCluster]
    kids: KidsContent
    primary_biome: Biome
    def __init__(self, id: _Optional[str] = ..., scientific_name: _Optional[str] = ..., common_name_pt: _Optional[str] = ..., family: _Optional[str] = ..., size_cm: _Optional[int] = ..., diet: _Optional[str] = ..., conservation_status: _Optional[_Union[ConservationStatus, str]] = ..., description: _Optional[str] = ..., description_credit: _Optional[_Union[Credit, _Mapping]] = ..., facts: _Optional[_Iterable[_Union[Fact, _Mapping]]] = ..., biomes: _Optional[_Iterable[_Union[Biome, str]]] = ..., states: _Optional[_Iterable[str]] = ..., photos: _Optional[_Iterable[_Union[Photo, _Mapping]]] = ..., audio: _Optional[_Union[Audio, _Mapping]] = ..., clusters: _Optional[_Iterable[_Union[OccurrenceCluster, _Mapping]]] = ..., kids: _Optional[_Union[KidsContent, _Mapping]] = ..., primary_biome: _Optional[_Union[Biome, str]] = ...) -> None: ...

class ListSpeciesRequest(_message.Message):
    __slots__ = ("query", "biome", "state", "page_size", "page_token", "kids_only", "primary_biome")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    BIOME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    KIDS_ONLY_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BIOME_FIELD_NUMBER: _ClassVar[int]
    query: str
    biome: Biome
    state: str
    page_size: int
    page_token: str
    kids_only: bool
    primary_biome: Biome
    def __init__(self, query: _Optional[str] = ..., biome: _Optional[_Union[Biome, str]] = ..., state: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., kids_only: _Optional[bool] = ..., primary_biome: _Optional[_Union[Biome, str]] = ...) -> None: ...

class ListSpeciesResponse(_message.Message):
    __slots__ = ("species", "next_page_token")
    SPECIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    species: _containers.RepeatedCompositeFieldContainer[SpeciesSummary]
    next_page_token: str
    def __init__(self, species: _Optional[_Iterable[_Union[SpeciesSummary, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSpeciesRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSpeciesResponse(_message.Message):
    __slots__ = ("species",)
    SPECIES_FIELD_NUMBER: _ClassVar[int]
    species: Species
    def __init__(self, species: _Optional[_Union[Species, _Mapping]] = ...) -> None: ...

class ListFiltersRequest(_message.Message):
    __slots__ = ("kids_only",)
    KIDS_ONLY_FIELD_NUMBER: _ClassVar[int]
    kids_only: bool
    def __init__(self, kids_only: _Optional[bool] = ...) -> None: ...

class BiomeCount(_message.Message):
    __slots__ = ("biome", "species_count")
    BIOME_FIELD_NUMBER: _ClassVar[int]
    SPECIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    biome: Biome
    species_count: int
    def __init__(self, biome: _Optional[_Union[Biome, str]] = ..., species_count: _Optional[int] = ...) -> None: ...

class StateCount(_message.Message):
    __slots__ = ("state", "species_count")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SPECIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    state: str
    species_count: int
    def __init__(self, state: _Optional[str] = ..., species_count: _Optional[int] = ...) -> None: ...

class ListFiltersResponse(_message.Message):
    __slots__ = ("biomes", "states", "primary_biome_counts")
    BIOMES_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BIOME_COUNTS_FIELD_NUMBER: _ClassVar[int]
    biomes: _containers.RepeatedCompositeFieldContainer[BiomeCount]
    states: _containers.RepeatedCompositeFieldContainer[StateCount]
    primary_biome_counts: _containers.RepeatedCompositeFieldContainer[BiomeCount]
    def __init__(self, biomes: _Optional[_Iterable[_Union[BiomeCount, _Mapping]]] = ..., states: _Optional[_Iterable[_Union[StateCount, _Mapping]]] = ..., primary_biome_counts: _Optional[_Iterable[_Union[BiomeCount, _Mapping]]] = ...) -> None: ...

class KidsFact(_message.Message):
    __slots__ = ("text", "source_fact")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FACT_FIELD_NUMBER: _ClassVar[int]
    text: str
    source_fact: int
    def __init__(self, text: _Optional[str] = ..., source_fact: _Optional[int] = ...) -> None: ...

class KidsContent(_message.Message):
    __slots__ = ("description", "facts", "did_you_know")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    DID_YOU_KNOW_FIELD_NUMBER: _ClassVar[int]
    description: str
    facts: _containers.RepeatedCompositeFieldContainer[KidsFact]
    did_you_know: str
    def __init__(self, description: _Optional[str] = ..., facts: _Optional[_Iterable[_Union[KidsFact, _Mapping]]] = ..., did_you_know: _Optional[str] = ...) -> None: ...

class GetFeaturedSpeciesRequest(_message.Message):
    __slots__ = ("date",)
    DATE_FIELD_NUMBER: _ClassVar[int]
    date: str
    def __init__(self, date: _Optional[str] = ...) -> None: ...

class GetFeaturedSpeciesResponse(_message.Message):
    __slots__ = ("species", "audio")
    SPECIES_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    species: SpeciesSummary
    audio: Audio
    def __init__(self, species: _Optional[_Union[SpeciesSummary, _Mapping]] = ..., audio: _Optional[_Union[Audio, _Mapping]] = ...) -> None: ...
