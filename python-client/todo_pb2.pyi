from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NewTodo(_message.Message):
    __slots__ = ("name", "description", "done")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    done: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., done: bool = ...) -> None: ...

class Todo(_message.Message):
    __slots__ = ("name", "description", "done", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    done: bool
    id: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., done: bool = ..., id: _Optional[str] = ...) -> None: ...
