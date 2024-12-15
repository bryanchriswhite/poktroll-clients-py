from poktroll_clients import (
    go_ref,
    ffi,
    libpoktroll_clients,
    GoManagedMem,
)


class QueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_url: str):
        self_ref = libpoktroll_clients.NewQueryClient(query_node_rpc_url.encode('utf-8'),
                                                         self.err_ptr)
        super().__init__(self_ref)
