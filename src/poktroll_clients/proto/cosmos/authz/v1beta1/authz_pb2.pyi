"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.43"""

import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenericAuthorization(google.protobuf.message.Message):
    """GenericAuthorization gives the grantee unrestricted permissions to execute
    the provided method on behalf of the granter's account.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MSG_FIELD_NUMBER: builtins.int
    msg: builtins.str
    """Msg, identified by it's type URL, to grant unrestricted permissions to execute"""
    def __init__(
        self,
        *,
        msg: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["msg", b"msg"]) -> None: ...

global___GenericAuthorization = GenericAuthorization

@typing.final
class Grant(google.protobuf.message.Message):
    """Grant gives permissions to execute
    the provide method with expiration time.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORIZATION_FIELD_NUMBER: builtins.int
    EXPIRATION_FIELD_NUMBER: builtins.int
    @property
    def authorization(self) -> google.protobuf.any_pb2.Any: ...
    @property
    def expiration(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """time when the grant will expire and will be pruned. If null, then the grant
        doesn't have a time expiration (other conditions  in `authorization`
        may apply to invalidate the grant)
        """

    def __init__(
        self,
        *,
        authorization: google.protobuf.any_pb2.Any | None = ...,
        expiration: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["authorization", b"authorization", "expiration", b"expiration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authorization", b"authorization", "expiration", b"expiration"]) -> None: ...

global___Grant = Grant

@typing.final
class GrantAuthorization(google.protobuf.message.Message):
    """GrantAuthorization extends a grant with both the addresses of the grantee and granter.
    It is used in genesis.proto and query.proto
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    AUTHORIZATION_FIELD_NUMBER: builtins.int
    EXPIRATION_FIELD_NUMBER: builtins.int
    granter: builtins.str
    grantee: builtins.str
    @property
    def authorization(self) -> google.protobuf.any_pb2.Any: ...
    @property
    def expiration(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        granter: builtins.str = ...,
        grantee: builtins.str = ...,
        authorization: google.protobuf.any_pb2.Any | None = ...,
        expiration: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["authorization", b"authorization", "expiration", b"expiration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authorization", b"authorization", "expiration", b"expiration", "grantee", b"grantee", "granter", b"granter"]) -> None: ...

global___GrantAuthorization = GrantAuthorization

@typing.final
class GrantQueueItem(google.protobuf.message.Message):
    """GrantQueueItem contains the list of TypeURL of a sdk.Msg."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MSG_TYPE_URLS_FIELD_NUMBER: builtins.int
    @property
    def msg_type_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """msg_type_urls contains the list of TypeURL of a sdk.Msg."""

    def __init__(
        self,
        *,
        msg_type_urls: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["msg_type_urls", b"msg_type_urls"]) -> None: ...

global___GrantQueueItem = GrantQueueItem