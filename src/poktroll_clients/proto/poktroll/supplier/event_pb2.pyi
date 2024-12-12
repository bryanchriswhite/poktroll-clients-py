"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import poktroll.shared.supplier_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SupplierUnbondingReason:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SupplierUnbondingReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SupplierUnbondingReason.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SUPPLIER_UNBONDING_REASON_UNSPECIFIED: _SupplierUnbondingReason.ValueType  # 0
    SUPPLIER_UNBONDING_REASON_VOLUNTARY: _SupplierUnbondingReason.ValueType  # 1
    SUPPLIER_UNBONDING_REASON_BELOW_MIN_STAKE: _SupplierUnbondingReason.ValueType  # 2

class SupplierUnbondingReason(_SupplierUnbondingReason, metaclass=_SupplierUnbondingReasonEnumTypeWrapper): ...

SUPPLIER_UNBONDING_REASON_UNSPECIFIED: SupplierUnbondingReason.ValueType  # 0
SUPPLIER_UNBONDING_REASON_VOLUNTARY: SupplierUnbondingReason.ValueType  # 1
SUPPLIER_UNBONDING_REASON_BELOW_MIN_STAKE: SupplierUnbondingReason.ValueType  # 2
global___SupplierUnbondingReason = SupplierUnbondingReason

@typing.final
class EventSupplierStaked(google.protobuf.message.Message):
    """EventSupplierStaked is emitted when a supplier stake message is committed on-chain."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    session_end_height: builtins.int
    """The session end height of the last session in which the supplier was staked."""
    @property
    def supplier(self) -> poktroll.shared.supplier_pb2.Supplier: ...
    def __init__(
        self,
        *,
        supplier: poktroll.shared.supplier_pb2.Supplier | None = ...,
        session_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["supplier", b"supplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["session_end_height", b"session_end_height", "supplier", b"supplier"]) -> None: ...

global___EventSupplierStaked = EventSupplierStaked

@typing.final
class EventSupplierUnbondingBegin(google.protobuf.message.Message):
    """EventSupplierUnbondingBegin is emitted when an application unstake message
    is committed on-chain, indicating that the supplier will now begin unbonding.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    UNBONDING_END_HEIGHT_FIELD_NUMBER: builtins.int
    reason: global___SupplierUnbondingReason.ValueType
    session_end_height: builtins.int
    """The session end height of the last session in which the supplier unbonding began."""
    unbonding_end_height: builtins.int
    """The height at which supplier unbonding will end."""
    @property
    def supplier(self) -> poktroll.shared.supplier_pb2.Supplier: ...
    def __init__(
        self,
        *,
        supplier: poktroll.shared.supplier_pb2.Supplier | None = ...,
        reason: global___SupplierUnbondingReason.ValueType = ...,
        session_end_height: builtins.int = ...,
        unbonding_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["supplier", b"supplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["reason", b"reason", "session_end_height", b"session_end_height", "supplier", b"supplier", "unbonding_end_height", b"unbonding_end_height"]) -> None: ...

global___EventSupplierUnbondingBegin = EventSupplierUnbondingBegin

@typing.final
class EventSupplierUnbondingEnd(google.protobuf.message.Message):
    """EventSupplierUnbondingEnd is emitted when an supplier has completed
    unbonding. The unbonding period is determined by the shared param,
    supplier_unbonding_period_sessions.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    UNBONDING_END_HEIGHT_FIELD_NUMBER: builtins.int
    reason: global___SupplierUnbondingReason.ValueType
    session_end_height: builtins.int
    """The session end height of the session in which the supplier unbonding endeded."""
    unbonding_end_height: builtins.int
    """The height at which supplier unbonding will end."""
    @property
    def supplier(self) -> poktroll.shared.supplier_pb2.Supplier: ...
    def __init__(
        self,
        *,
        supplier: poktroll.shared.supplier_pb2.Supplier | None = ...,
        reason: global___SupplierUnbondingReason.ValueType = ...,
        session_end_height: builtins.int = ...,
        unbonding_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["supplier", b"supplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["reason", b"reason", "session_end_height", b"session_end_height", "supplier", b"supplier", "unbonding_end_height", b"unbonding_end_height"]) -> None: ...

global___EventSupplierUnbondingEnd = EventSupplierUnbondingEnd

@typing.final
class EventSupplierUnbondingCanceled(google.protobuf.message.Message):
    """EventSupplierUnbondingCanceled is emitted when an supplier which was unbonding
    successfully (re-)stakes before the unbonding period has elapsed. An EventSupplierStaked
    event will also be emitted immediately after this event.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    height: builtins.int
    """The exact height at which the supplier unbonding was canceled."""
    session_end_height: builtins.int
    """The session end height of the session in which the supplier unbonding was canceled."""
    @property
    def supplier(self) -> poktroll.shared.supplier_pb2.Supplier: ...
    def __init__(
        self,
        *,
        supplier: poktroll.shared.supplier_pb2.Supplier | None = ...,
        height: builtins.int = ...,
        session_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["supplier", b"supplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "session_end_height", b"session_end_height", "supplier", b"supplier"]) -> None: ...

global___EventSupplierUnbondingCanceled = EventSupplierUnbondingCanceled