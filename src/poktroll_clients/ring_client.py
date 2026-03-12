from poktroll_clients.ffi import ffi, libpoktroll_clients
from poktroll_clients.go_memory import GoManagedMem, go_ref, check_err, check_ref


class RingClient(GoManagedMem):
    """Signs relay requests using ring signatures.

    Uses the application's delegated gateways to construct a ring and signs
    relay requests for Pocket protocol authentication.

    Requires a QueryClient reference (from NewQueryClient) which provides
    access to application, account, and shared parameter queries needed
    for ring construction.
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_client_ref: go_ref):
        """
        Construct a RingClient from a QueryClient reference.

        :param query_client_ref: A go_ref to a MultiQueryClient (from QueryClient).
        """
        go_ref = libpoktroll_clients.NewRingClient(query_client_ref, self.err_ptr)
        super().__init__(go_ref)

    def sign_relay_request(self, private_key: bytes, relay_request_bz: bytes) -> bytes:
        """
        Sign a serialized RelayRequest with a ring signature.

        The ring is constructed from the application's delegated gateways
        (looked up via the session header in the relay request). The private
        key must belong to a member of the ring (the app or a delegated gateway).

        :param private_key: Raw secp256k1 private key bytes (32 bytes).
        :param relay_request_bz: Serialized RelayRequest protobuf bytes.
        :return: Serialized ring signature bytes.
        :raises FFIError: If signing fails (e.g., key not in ring, invalid request).
        """
        err_ptr = ffi.new("char **")
        out_sig_bz = ffi.new("uint8_t **")
        out_sig_len = ffi.new("size_t *")

        libpoktroll_clients.RingClient_SignRelayRequest(
            self.go_ref,
            private_key, len(private_key),
            relay_request_bz, len(relay_request_bz),
            out_sig_bz, out_sig_len,
            err_ptr,
        )
        check_err(err_ptr)

        sig_len = out_sig_len[0]
        if sig_len == 0 or out_sig_bz[0] == ffi.NULL:
            raise ValueError("RingClient_SignRelayRequest returned empty signature")

        # Copy from C-allocated memory to Python bytes.
        # NOTE: The C memory (allocated via C.malloc in Go) is not freed here.
        # This is a small leak per signing operation. A proper fix would add a
        # FreeCBytes CGo export or use Go-managed memory instead of C.malloc.
        # Acceptable for the prototype; tracked for Path B cleanup.
        signature = bytes(ffi.buffer(out_sig_bz[0], sig_len))
        return signature
