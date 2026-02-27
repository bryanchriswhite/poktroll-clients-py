from typing import List

from cffi import FFIError

from poktroll_clients.ffi import ffi, libpoktroll_clients
from poktroll_clients.go_memory import GoManagedMem, go_ref, check_err
from poktroll_clients.protobuf import SerializedProto, ProtoMessageArray, deserialize_proto

from poktroll_clients.proto.pocket.migration import tx_pb2 as migration_tx_pb2
from poktroll_clients.proto.pocket.shared import service_pb2


class MorseKeyManager(GoManagedMem):
    """
    Manages a Morse private key and creates signed claim messages for the Morse-to-Shannon migration.

    Wraps the Morse key management and claim message C functions from libpoktroll-clients.
    The underlying Go-managed private key is freed automatically when this object is garbage collected.
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, morse_key_export_path: str, passphrase: str = ""):
        """
        Load a Morse private key from an export file.
        :param morse_key_export_path: Path to the Morse key export JSON file.
        :param passphrase: Decryption passphrase. Empty string if key is unencrypted.
        """
        err_ptr = ffi.new("char **")
        ref = libpoktroll_clients.LoadMorsePrivateKey(
            morse_key_export_path.encode('utf-8'),
            passphrase.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        super().__init__(ref)

    @property
    def morse_address(self) -> str:
        """Get the hex-encoded Morse address derived from the loaded private key."""
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.GetMorseAddress(self.go_ref, err_ptr)
        check_err(err_ptr)
        if result == ffi.NULL:
            raise FFIError("null morse address")
        return ffi.string(result).decode('utf-8')

    def new_msg_claim_morse_account(
        self,
        shannon_dest_addr: str,
        shannon_signing_addr: str,
    ) -> migration_tx_pb2.MsgClaimMorseAccount:
        """
        Create a signed MsgClaimMorseAccount for claiming a Morse account balance.
        :param shannon_dest_addr: Bech32 Shannon address to receive claimed tokens.
        :param shannon_signing_addr: Bech32 Shannon address of the transaction signer.
        :return: A fully signed MsgClaimMorseAccount ready for broadcast.
        """
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.NewSerializedSignedMsgClaimMorseAccount(
            shannon_dest_addr.encode('utf-8'),
            self.go_ref,
            shannon_signing_addr.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, migration_tx_pb2.MsgClaimMorseAccount)

    def new_msg_claim_morse_application(
        self,
        shannon_dest_addr: str,
        service_id: str,
        shannon_signing_addr: str,
    ) -> migration_tx_pb2.MsgClaimMorseApplication:
        """
        Create a signed MsgClaimMorseApplication for claiming and staking as an application.
        :param shannon_dest_addr: Bech32 Shannon address to receive claimed tokens.
        :param service_id: Service ID to stake the application for.
        :param shannon_signing_addr: Bech32 Shannon address of the transaction signer.
        :return: A fully signed MsgClaimMorseApplication ready for broadcast.
        """
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.NewSerializedSignedMsgClaimMorseApplication(
            shannon_dest_addr.encode('utf-8'),
            self.go_ref,
            service_id.encode('utf-8'),
            shannon_signing_addr.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, migration_tx_pb2.MsgClaimMorseApplication)

    def new_msg_claim_morse_supplier(
        self,
        shannon_owner_addr: str,
        shannon_operator_addr: str,
        morse_node_addr: str,
        supplier_service_configs: List[service_pb2.SupplierServiceConfig],
        shannon_signing_addr: str,
    ) -> migration_tx_pb2.MsgClaimMorseSupplier:
        """
        Create a signed MsgClaimMorseSupplier for claiming and staking as a supplier.
        :param shannon_owner_addr: Bech32 Shannon owner address.
        :param shannon_operator_addr: Bech32 Shannon operator address.
        :param morse_node_addr: The Morse node address associated with the supplier.
        :param supplier_service_configs: List of SupplierServiceConfig protos for the supplier.
        :param shannon_signing_addr: Bech32 Shannon address of the transaction signer.
        :return: A fully signed MsgClaimMorseSupplier ready for broadcast.
        """
        serialized_configs = ProtoMessageArray(messages=[
            SerializedProto(
                type_url=cfg.DESCRIPTOR.full_name,
                data=cfg.SerializeToString(),
            )
            for cfg in supplier_service_configs
        ])
        c_configs = serialized_configs.to_c_struct()

        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.NewSerializedSignedMsgClaimMorseSupplier(
            shannon_owner_addr.encode('utf-8'),
            shannon_operator_addr.encode('utf-8'),
            morse_node_addr.encode('utf-8'),
            self.go_ref,
            c_configs,
            shannon_signing_addr.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, migration_tx_pb2.MsgClaimMorseSupplier)

    def sign_morse_claim_msg(self, msg_type_url: str, msg_data: bytes) -> bytes:
        """
        Low-level: sign an already-serialized claim message with the Morse private key.
        :param msg_type_url: The protobuf type URL of the message.
        :param msg_data: The serialized protobuf bytes.
        :return: 64-byte ed25519 signature.
        """
        serialized = SerializedProto(type_url=msg_type_url, data=msg_data)
        c_proto = serialized.to_c_struct()

        sig_buf = ffi.new("uint8_t[64]")
        err_ptr = ffi.new("char **")
        libpoktroll_clients.SignMorseClaimMsg(c_proto, self.go_ref, sig_buf, err_ptr)
        check_err(err_ptr)
        return bytes(ffi.buffer(sig_buf, 64))
