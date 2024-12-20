"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import cosmos.crypto.multisig.v1beta1.multisig_pb2
import cosmos.tx.signing.v1beta1.signing_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Tx(google.protobuf.message.Message):
    """Tx is the standard type used for broadcasting transactions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_FIELD_NUMBER: builtins.int
    AUTH_INFO_FIELD_NUMBER: builtins.int
    SIGNATURES_FIELD_NUMBER: builtins.int
    @property
    def body(self) -> global___TxBody:
        """body is the processable content of the transaction"""

    @property
    def auth_info(self) -> global___AuthInfo:
        """auth_info is the authorization related content of the transaction,
        specifically signers, signer modes and fee
        """

    @property
    def signatures(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """signatures is a list of signatures that matches the length and order of
        AuthInfo's signer_infos to allow connecting signature meta information like
        public key and signing mode by position.
        """

    def __init__(
        self,
        *,
        body: global___TxBody | None = ...,
        auth_info: global___AuthInfo | None = ...,
        signatures: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auth_info", b"auth_info", "body", b"body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auth_info", b"auth_info", "body", b"body", "signatures", b"signatures"]) -> None: ...

global___Tx = Tx

@typing.final
class TxRaw(google.protobuf.message.Message):
    """TxRaw is a variant of Tx that pins the signer's exact binary representation
    of body and auth_info. This is used for signing, broadcasting and
    verification. The binary `serialize(tx: TxRaw)` is stored in Tendermint and
    the hash `sha256(serialize(tx: TxRaw))` becomes the "txhash", commonly used
    as the transaction ID.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_BYTES_FIELD_NUMBER: builtins.int
    AUTH_INFO_BYTES_FIELD_NUMBER: builtins.int
    SIGNATURES_FIELD_NUMBER: builtins.int
    body_bytes: builtins.bytes
    """body_bytes is a protobuf serialization of a TxBody that matches the
    representation in SignDoc.
    """
    auth_info_bytes: builtins.bytes
    """auth_info_bytes is a protobuf serialization of an AuthInfo that matches the
    representation in SignDoc.
    """
    @property
    def signatures(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """signatures is a list of signatures that matches the length and order of
        AuthInfo's signer_infos to allow connecting signature meta information like
        public key and signing mode by position.
        """

    def __init__(
        self,
        *,
        body_bytes: builtins.bytes = ...,
        auth_info_bytes: builtins.bytes = ...,
        signatures: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["auth_info_bytes", b"auth_info_bytes", "body_bytes", b"body_bytes", "signatures", b"signatures"]) -> None: ...

global___TxRaw = TxRaw

@typing.final
class SignDoc(google.protobuf.message.Message):
    """SignDoc is the type used for generating sign bytes for SIGN_MODE_DIRECT."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_BYTES_FIELD_NUMBER: builtins.int
    AUTH_INFO_BYTES_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    ACCOUNT_NUMBER_FIELD_NUMBER: builtins.int
    body_bytes: builtins.bytes
    """body_bytes is protobuf serialization of a TxBody that matches the
    representation in TxRaw.
    """
    auth_info_bytes: builtins.bytes
    """auth_info_bytes is a protobuf serialization of an AuthInfo that matches the
    representation in TxRaw.
    """
    chain_id: builtins.str
    """chain_id is the unique identifier of the chain this transaction targets.
    It prevents signed transactions from being used on another chain by an
    attacker
    """
    account_number: builtins.int
    """account_number is the account number of the account in state"""
    def __init__(
        self,
        *,
        body_bytes: builtins.bytes = ...,
        auth_info_bytes: builtins.bytes = ...,
        chain_id: builtins.str = ...,
        account_number: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["account_number", b"account_number", "auth_info_bytes", b"auth_info_bytes", "body_bytes", b"body_bytes", "chain_id", b"chain_id"]) -> None: ...

global___SignDoc = SignDoc

@typing.final
class SignDocDirectAux(google.protobuf.message.Message):
    """SignDocDirectAux is the type used for generating sign bytes for
    SIGN_MODE_DIRECT_AUX.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_BYTES_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    ACCOUNT_NUMBER_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    TIP_FIELD_NUMBER: builtins.int
    body_bytes: builtins.bytes
    """body_bytes is protobuf serialization of a TxBody that matches the
    representation in TxRaw.
    """
    chain_id: builtins.str
    """chain_id is the identifier of the chain this transaction targets.
    It prevents signed transactions from being used on another chain by an
    attacker.
    """
    account_number: builtins.int
    """account_number is the account number of the account in state."""
    sequence: builtins.int
    """sequence is the sequence number of the signing account."""
    @property
    def public_key(self) -> google.protobuf.any_pb2.Any:
        """public_key is the public key of the signing account."""

    @property
    def tip(self) -> global___Tip:
        """tips have been deprecated and should not be used"""

    def __init__(
        self,
        *,
        body_bytes: builtins.bytes = ...,
        public_key: google.protobuf.any_pb2.Any | None = ...,
        chain_id: builtins.str = ...,
        account_number: builtins.int = ...,
        sequence: builtins.int = ...,
        tip: global___Tip | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["public_key", b"public_key", "tip", b"tip"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["account_number", b"account_number", "body_bytes", b"body_bytes", "chain_id", b"chain_id", "public_key", b"public_key", "sequence", b"sequence", "tip", b"tip"]) -> None: ...

global___SignDocDirectAux = SignDocDirectAux

@typing.final
class TxBody(google.protobuf.message.Message):
    """TxBody is the body of a transaction that all signers sign over."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGES_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    TIMEOUT_HEIGHT_FIELD_NUMBER: builtins.int
    UNORDERED_FIELD_NUMBER: builtins.int
    EXTENSION_OPTIONS_FIELD_NUMBER: builtins.int
    NON_CRITICAL_EXTENSION_OPTIONS_FIELD_NUMBER: builtins.int
    memo: builtins.str
    """memo is any arbitrary note/comment to be added to the transaction.
    WARNING: in clients, any publicly exposed text should not be called memo,
    but should be called `note` instead (see
    https://github.com/cosmos/cosmos-sdk/issues/9122).
    """
    timeout_height: builtins.int
    """timeout_height is the block height after which this transaction will not
    be processed by the chain.

    Note, if unordered=true this value MUST be set
    and will act as a short-lived TTL in which the transaction is deemed valid
    and kept in memory to prevent duplicates.
    """
    unordered: builtins.bool
    """unordered, when set to true, indicates that the transaction signer(s)
    intend for the transaction to be evaluated and executed in an un-ordered
    fashion. Specifically, the account's nonce will NOT be checked or
    incremented, which allows for fire-and-forget as well as concurrent
    transaction execution.

    Note, when set to true, the existing 'timeout_height' value must be set and
    will be used to correspond to a height in which the transaction is deemed
    valid.
    """
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """messages is a list of messages to be executed. The required signers of
        those messages define the number and order of elements in AuthInfo's
        signer_infos and Tx's signatures. Each required signer address is added to
        the list only the first time it occurs.
        By convention, the first required signer (usually from the first message)
        is referred to as the primary signer and pays the fee for the whole
        transaction.
        """

    @property
    def extension_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """extension_options are arbitrary options that can be added by chains
        when the default options are not sufficient. If any of these are present
        and can't be handled, the transaction will be rejected
        """

    @property
    def non_critical_extension_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """extension_options are arbitrary options that can be added by chains
        when the default options are not sufficient. If any of these are present
        and can't be handled, they will be ignored
        """

    def __init__(
        self,
        *,
        messages: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        memo: builtins.str = ...,
        timeout_height: builtins.int = ...,
        unordered: builtins.bool = ...,
        extension_options: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        non_critical_extension_options: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["extension_options", b"extension_options", "memo", b"memo", "messages", b"messages", "non_critical_extension_options", b"non_critical_extension_options", "timeout_height", b"timeout_height", "unordered", b"unordered"]) -> None: ...

global___TxBody = TxBody

@typing.final
class AuthInfo(google.protobuf.message.Message):
    """AuthInfo describes the fee and signer modes that are used to sign a
    transaction.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIGNER_INFOS_FIELD_NUMBER: builtins.int
    FEE_FIELD_NUMBER: builtins.int
    TIP_FIELD_NUMBER: builtins.int
    @property
    def signer_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SignerInfo]:
        """signer_infos defines the signing modes for the required signers. The number
        and order of elements must match the required signers from TxBody's
        messages. The first element is the primary signer and the one which pays
        the fee.
        """

    @property
    def fee(self) -> global___Fee:
        """Fee is the fee and gas limit for the transaction. The first signer is the
        primary signer and the one which pays the fee. The fee can be calculated
        based on the cost of evaluating the body and doing signature verification
        of the signers. This can be estimated via simulation.
        """

    @property
    def tip(self) -> global___Tip:
        """Tip is the optional tip used for transactions fees paid in another denom.

        This field is ignored if the chain didn't enable tips, i.e. didn't add the
        `TipDecorator` in its posthandler.

        Since: cosmos-sdk 0.46
        """

    def __init__(
        self,
        *,
        signer_infos: collections.abc.Iterable[global___SignerInfo] | None = ...,
        fee: global___Fee | None = ...,
        tip: global___Tip | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["fee", b"fee", "tip", b"tip"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["fee", b"fee", "signer_infos", b"signer_infos", "tip", b"tip"]) -> None: ...

global___AuthInfo = AuthInfo

@typing.final
class SignerInfo(google.protobuf.message.Message):
    """SignerInfo describes the public key and signing mode of a single top-level
    signer.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    MODE_INFO_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    sequence: builtins.int
    """sequence is the sequence of the account, which describes the
    number of committed transactions signed by a given address. It is used to
    prevent replay attacks.
    """
    @property
    def public_key(self) -> google.protobuf.any_pb2.Any:
        """public_key is the public key of the signer. It is optional for accounts
        that already exist in state. If unset, the verifier can use the required \\
        signer address for this position and lookup the public key.
        """

    @property
    def mode_info(self) -> global___ModeInfo:
        """mode_info describes the signing mode of the signer and is a nested
        structure to support nested multisig pubkey's
        """

    def __init__(
        self,
        *,
        public_key: google.protobuf.any_pb2.Any | None = ...,
        mode_info: global___ModeInfo | None = ...,
        sequence: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["mode_info", b"mode_info", "public_key", b"public_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["mode_info", b"mode_info", "public_key", b"public_key", "sequence", b"sequence"]) -> None: ...

global___SignerInfo = SignerInfo

@typing.final
class ModeInfo(google.protobuf.message.Message):
    """ModeInfo describes the signing mode of a single or nested multisig signer."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Single(google.protobuf.message.Message):
        """Single is the mode info for a single signer. It is structured as a message
        to allow for additional fields such as locale for SIGN_MODE_TEXTUAL in the
        future
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MODE_FIELD_NUMBER: builtins.int
        mode: cosmos.tx.signing.v1beta1.signing_pb2.SignMode.ValueType
        """mode is the signing mode of the single signer"""
        def __init__(
            self,
            *,
            mode: cosmos.tx.signing.v1beta1.signing_pb2.SignMode.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["mode", b"mode"]) -> None: ...

    @typing.final
    class Multi(google.protobuf.message.Message):
        """Multi is the mode info for a multisig public key"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BITARRAY_FIELD_NUMBER: builtins.int
        MODE_INFOS_FIELD_NUMBER: builtins.int
        @property
        def bitarray(self) -> cosmos.crypto.multisig.v1beta1.multisig_pb2.CompactBitArray:
            """bitarray specifies which keys within the multisig are signing"""

        @property
        def mode_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModeInfo]:
            """mode_infos is the corresponding modes of the signers of the multisig
            which could include nested multisig public keys
            """

        def __init__(
            self,
            *,
            bitarray: cosmos.crypto.multisig.v1beta1.multisig_pb2.CompactBitArray | None = ...,
            mode_infos: collections.abc.Iterable[global___ModeInfo] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["bitarray", b"bitarray"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["bitarray", b"bitarray", "mode_infos", b"mode_infos"]) -> None: ...

    SINGLE_FIELD_NUMBER: builtins.int
    MULTI_FIELD_NUMBER: builtins.int
    @property
    def single(self) -> global___ModeInfo.Single:
        """single represents a single signer"""

    @property
    def multi(self) -> global___ModeInfo.Multi:
        """multi represents a nested multisig signer"""

    def __init__(
        self,
        *,
        single: global___ModeInfo.Single | None = ...,
        multi: global___ModeInfo.Multi | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["multi", b"multi", "single", b"single", "sum", b"sum"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["multi", b"multi", "single", b"single", "sum", b"sum"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sum", b"sum"]) -> typing.Literal["single", "multi"] | None: ...

global___ModeInfo = ModeInfo

@typing.final
class Fee(google.protobuf.message.Message):
    """Fee includes the amount of coins paid in fees and the maximum
    gas to be used by the transaction. The ratio yields an effective "gasprice",
    which must be above some miminum to be accepted into the mempool.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMOUNT_FIELD_NUMBER: builtins.int
    GAS_LIMIT_FIELD_NUMBER: builtins.int
    PAYER_FIELD_NUMBER: builtins.int
    GRANTER_FIELD_NUMBER: builtins.int
    gas_limit: builtins.int
    """gas_limit is the maximum gas that can be used in transaction processing
    before an out of gas error occurs
    """
    payer: builtins.str
    """if unset, the first signer is responsible for paying the fees. If set, the
    specified account must pay the fees. the payer must be a tx signer (and
    thus have signed this field in AuthInfo). setting this field does *not*
    change the ordering of required signers for the transaction.
    """
    granter: builtins.str
    """if set, the fee payer (either the first signer or the value of the payer
    field) requests that a fee grant be used to pay fees instead of the fee
    payer's own balance. If an appropriate fee grant does not exist or the
    chain does not support fee grants, this will fail
    """
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """amount is the amount of coins to be paid as a fee"""

    def __init__(
        self,
        *,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        gas_limit: builtins.int = ...,
        payer: builtins.str = ...,
        granter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount", b"amount", "gas_limit", b"gas_limit", "granter", b"granter", "payer", b"payer"]) -> None: ...

global___Fee = Fee

@typing.final
class Tip(google.protobuf.message.Message):
    """Tip is the tip used for meta-transactions.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMOUNT_FIELD_NUMBER: builtins.int
    TIPPER_FIELD_NUMBER: builtins.int
    tipper: builtins.str
    """tipper is the address of the account paying for the tip"""
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """amount is the amount of the tip"""

    def __init__(
        self,
        *,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        tipper: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount", b"amount", "tipper", b"tipper"]) -> None: ...

global___Tip = Tip

@typing.final
class AuxSignerData(google.protobuf.message.Message):
    """AuxSignerData is the intermediary format that an auxiliary signer (e.g. a
    tipper) builds and sends to the fee payer (who will build and broadcast the
    actual tx). AuxSignerData is not a valid tx in itself, and will be rejected
    by the node if sent directly as-is.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    SIGN_DOC_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    SIG_FIELD_NUMBER: builtins.int
    address: builtins.str
    """address is the bech32-encoded address of the auxiliary signer. If using
    AuxSignerData across different chains, the bech32 prefix of the target
    chain (where the final transaction is broadcasted) should be used.
    """
    mode: cosmos.tx.signing.v1beta1.signing_pb2.SignMode.ValueType
    """mode is the signing mode of the single signer."""
    sig: builtins.bytes
    """sig is the signature of the sign doc."""
    @property
    def sign_doc(self) -> global___SignDocDirectAux:
        """sign_doc is the SIGN_MODE_DIRECT_AUX sign doc that the auxiliary signer
        signs. Note: we use the same sign doc even if we're signing with
        LEGACY_AMINO_JSON.
        """

    def __init__(
        self,
        *,
        address: builtins.str = ...,
        sign_doc: global___SignDocDirectAux | None = ...,
        mode: cosmos.tx.signing.v1beta1.signing_pb2.SignMode.ValueType = ...,
        sig: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["sign_doc", b"sign_doc"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "mode", b"mode", "sig", b"sig", "sign_doc", b"sign_doc"]) -> None: ...

global___AuxSignerData = AuxSignerData
