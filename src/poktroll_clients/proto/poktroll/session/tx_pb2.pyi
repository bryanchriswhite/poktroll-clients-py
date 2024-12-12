"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import poktroll.session.params_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgUpdateParams(google.protobuf.message.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    @property
    def params(self) -> poktroll.session.params_pb2.Params:
        """TODO_IMPROVE(#322): The requirement to provide all params is adopted from the
        latest Cosmos SDK version. We should look into either improving this ourselves
        or seeing if it is on their roadmap.

        params defines the x/session parameters to update.
        NOTE: All parameters must be supplied.
        """

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: poktroll.session.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdateParams = MsgUpdateParams

@typing.final
class MsgUpdateParamsResponse(google.protobuf.message.Message):
    """MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateParamsResponse = MsgUpdateParamsResponse

@typing.final
class MsgUpdateParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    AS_UINT64_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    name: builtins.str
    as_uint64: builtins.int
    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        name: builtins.str = ...,
        as_uint64: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["as_type", b"as_type", "as_uint64", b"as_uint64"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["as_type", b"as_type", "as_uint64", b"as_uint64", "authority", b"authority", "name", b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["as_type", b"as_type"]) -> typing.Literal["as_uint64"] | None: ...

global___MsgUpdateParam = MsgUpdateParam

@typing.final
class MsgUpdateParamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> poktroll.session.params_pb2.Params: ...
    def __init__(
        self,
        *,
        params: poktroll.session.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___MsgUpdateParamResponse = MsgUpdateParamResponse