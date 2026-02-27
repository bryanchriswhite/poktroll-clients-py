from poktroll_clients.ffi import ffi, libpoktroll_clients
from poktroll_clients.go_memory import GoManagedMem, go_ref, check_err, check_ref


class EventsQueryClient(GoManagedMem):
    """Subscribes to CometBFT events via WebSocket."""

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_websocket_url: str):
        go_ref = libpoktroll_clients.NewEventsQueryClient(query_node_rpc_websocket_url.encode('utf-8'))
        super().__init__(go_ref)

    def EventsBytes(self, query: str) -> go_ref:
        err_ptr = ffi.new("char **")
        ref = libpoktroll_clients.EventsQueryClientEventsBytes(self.go_ref, query.encode('utf-8'), err_ptr)
        check_err(err_ptr)
        check_ref(ref)
        return ref
