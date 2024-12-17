import asyncio
from typing import Tuple, Dict

from atomics import INTEGRAL, atomic, INT
from cffi import FFIError

from poktroll_clients import (
    go_ref,
    ffi,
    libpoktroll_clients,
    GoManagedMem, BlockQueryClient, Supply, check_err, check_ref,
)
from poktroll_clients.proto.poktroll.shared.params_pb2 import Params as SharedParams
from poktroll_clients.proto.poktroll.application.params_pb2 import Params as ApplicationParams
from poktroll_clients.proto.poktroll.gateway.params_pb2 import Params as GatewayParams
from poktroll_clients.proto.poktroll.supplier.params_pb2 import Params as SupplierParams
from poktroll_clients.proto.poktroll.session.params_pb2 import Params as SessionParams
from poktroll_clients.proto.poktroll.service.params_pb2 import Params as ServiceParams
from poktroll_clients.proto.poktroll.proof.params_pb2 import Params as ProofParams
from poktroll_clients.proto.poktroll.tokenomics.params_pb2 import Params as TokenomicsParams
from poktroll_clients.protobuf import get_proto_from_go_ref


class QueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData
    # _callback_idx: INTEGRAL = atomic(width=8, atype=INT)
    # _callback_fns: Dict[int, Tuple[ffi.CData, ffi.CData, ffi.CData]] = {}

    def __init__(self, query_node_rpc_url: str, deps_ref: go_ref = -1):
        if deps_ref == -1:
            deps_ref = _new_query_client_depinject_config(query_node_rpc_url)

        self_ref = libpoktroll_clients.NewQueryClient(deps_ref,
                                                      query_node_rpc_url.encode('utf-8'),
                                                      self.err_ptr)
        super().__init__(self_ref)

    # async def get_shared_params(self) -> asyncio.Future[SharedParams]:
    #     op, future = self._new_async_operation()
    #
    #     err_ch_ref = libpoktroll_clients.QueryClient_GetSharedParams(  # <-- line 71
    #         op,
    #         self.go_ref,
    #     )
    #
    #     if err_ch_ref == -1:
    #         error_msg = ffi.string(op.ctx.error_msg).decode('utf-8')
    #         future.set_exception(FFIError(error_msg))
    #
    #     return await future

    def get_shared_params(self) -> asyncio.Future[SharedParams]:
        response_ref = libpoktroll_clients.QueryClient_GetSharedParams(self.go_ref, self.err_ptr)
        check_err(self.err_ptr)
        check_ref(response_ref)

        return get_proto_from_go_ref(response_ref)

    def get_application_params(self) -> ApplicationParams:
        response_ref = libpoktroll_clients.QueryClient_GetApplicationParams(self.go_ref, self.err_ptr)

    def get_supplier_params(self) -> SupplierParams:
        response_ref = libpoktroll_clients.QueryClient_GetSupplierParams(self.go_ref, self.err_ptr)

    def get_gateway_params(self) -> GatewayParams:
        response_ref = libpoktroll_clients.QueryClient_GetGatewayParams(self.go_ref, self.err_ptr)

    def get_session_params(self) -> SessionParams:
        response_ref = libpoktroll_clients.QueryClient_GetSessionParams(self.go_ref, self.err_ptr)

    def get_service_params(self) -> ServiceParams:
        response_ref = libpoktroll_clients.QueryClient_GetServiceParams(self.go_ref, self.err_ptr)

    def get_proof_params(self) -> ProofParams:
        response_ref = libpoktroll_clients.QueryClient_GetProofParams(self.go_ref, self.err_ptr)

    def get_tokenomics_params(self) -> TokenomicsParams:
        response_ref = libpoktroll_clients.QueryClient_GetTokenomicsParams(self.go_ref, self.err_ptr)

    # TODO_CONSIDERATION: support an async API as well?

    # def _new_async_operation(self) -> Tuple[ffi.CData, asyncio.Future]:
    #     """
    #     Creates a new AsyncOperation with callbacks and associated Future.
    #     The callbacks are protected from garbage collection by storing in self._callback_fns.
    #
    #     TODO_IN_THIS_COMMIT: & de-duplicate w/ TxClient...
    #     """
    #
    #     try:
    #         loop = asyncio.get_running_loop()
    #     except RuntimeError:
    #         loop = asyncio.new_event_loop()
    #         asyncio.set_event_loop(loop)
    #
    #     future = loop.create_future()
    #
    #     # Create AsyncContext
    #     ctx = ffi.new("AsyncContext *")
    #     next_callback_idx = self._callback_idx.fetch_inc()
    #
    #     # Define callbacks
    #     @ffi.callback("void(AsyncContext*, const void*)")
    #     def success_cb(ctx: ffi.CData, response_ref: go_ref):
    #         try:
    #             print("success_cb")
    #             # serialized_proto_response = ffi.cast("serialized_proto*", response_ref)
    #             response = get_proto_from_go_ref(response_ref).params
    #             loop.call_soon_threadsafe(future.set_result, response)
    #         finally:
    #             self._free_callback(next_callback_idx)
    #
    #     @ffi.callback("void(AsyncContext*, const char*)")
    #     def error_cb(ctx, error):
    #         print("error_cb")
    #         try:
    #             error_str = ffi.string(error).decode('utf-8')
    #             loop.call_soon_threadsafe(future.set_exception, Exception(error_str))
    #         except Exception as e:
    #             future.set_exception(e)
    #         finally:
    #             self._free_callback(next_callback_idx)
    #
    #     @ffi.callback("void(AsyncContext*)")
    #     def cleanup_cb(ctx):
    #         self._free_callback(next_callback_idx)
    #
    #     # Create AsyncOperation
    #     op = ffi.new("AsyncOperation *")
    #     op.ctx = ctx
    #     op.on_success = success_cb
    #     op.on_error = error_cb
    #     op.cleanup = cleanup_cb
    #
    #     # Store callbacks to protect from garbage collection
    #     self._callback_fns[next_callback_idx] = (success_cb, error_cb, cleanup_cb)
    #
    #     return op, future

    def _free_callback(self, callback_idx: int):
        """
        Clean up stored callbacks.
        """
        self._callback_fns.pop(callback_idx)


def _new_query_client_depinject_config(
        query_node_rpc_url: str,
) -> go_ref:
    """
    TODO_IN_THIS_COMMIT: comment
    """

    # TODO_IN_THIS_COMMIT: add more detail to the error messages,
    # explaining the expected format, with an example.
    if not query_node_rpc_url:
        raise ValueError("query_node_rpc_url must be specified")

    block_query_client = BlockQueryClient(query_node_rpc_url)
    return Supply(block_query_client.go_ref)
