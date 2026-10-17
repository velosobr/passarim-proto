from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHOTO_CATEGORY_UNSPECIFIED: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_SINGLE_BIRD: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_FLOCK: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_NEST: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_EGGS: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_FEATHER: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_DEAD_BIRD: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_NO_BIRD: _ClassVar[PhotoCategory]
    PHOTO_CATEGORY_OTHER: _ClassVar[PhotoCategory]
PHOTO_CATEGORY_UNSPECIFIED: PhotoCategory
PHOTO_CATEGORY_SINGLE_BIRD: PhotoCategory
PHOTO_CATEGORY_FLOCK: PhotoCategory
PHOTO_CATEGORY_NEST: PhotoCategory
PHOTO_CATEGORY_EGGS: PhotoCategory
PHOTO_CATEGORY_FEATHER: PhotoCategory
PHOTO_CATEGORY_DEAD_BIRD: PhotoCategory
PHOTO_CATEGORY_NO_BIRD: PhotoCategory
PHOTO_CATEGORY_OTHER: PhotoCategory

class ClassifyPhotosRequest(_message.Message):
    __slots__ = ("photos",)
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    photos: _containers.RepeatedCompositeFieldContainer[PhotoInput]
    def __init__(self, photos: _Optional[_Iterable[_Union[PhotoInput, _Mapping]]] = ...) -> None: ...

class PhotoInput(_message.Message):
    __slots__ = ("photo_id", "image")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    photo_id: str
    image: bytes
    def __init__(self, photo_id: _Optional[str] = ..., image: _Optional[bytes] = ...) -> None: ...

class ClassifyPhotosResponse(_message.Message):
    __slots__ = ("verdicts", "model_version")
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    verdicts: _containers.RepeatedCompositeFieldContainer[PhotoVerdict]
    model_version: str
    def __init__(self, verdicts: _Optional[_Iterable[_Union[PhotoVerdict, _Mapping]]] = ..., model_version: _Optional[str] = ...) -> None: ...

class PhotoVerdict(_message.Message):
    __slots__ = ("photo_id", "category", "bird_count", "largest_bird_area", "largest_bird_cut", "sharpness", "confidence")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    BIRD_COUNT_FIELD_NUMBER: _ClassVar[int]
    LARGEST_BIRD_AREA_FIELD_NUMBER: _ClassVar[int]
    LARGEST_BIRD_CUT_FIELD_NUMBER: _ClassVar[int]
    SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    photo_id: str
    category: PhotoCategory
    bird_count: int
    largest_bird_area: float
    largest_bird_cut: bool
    sharpness: float
    confidence: float
    def __init__(self, photo_id: _Optional[str] = ..., category: _Optional[_Union[PhotoCategory, str]] = ..., bird_count: _Optional[int] = ..., largest_bird_area: _Optional[float] = ..., largest_bird_cut: _Optional[bool] = ..., sharpness: _Optional[float] = ..., confidence: _Optional[float] = ...) -> None: ...
