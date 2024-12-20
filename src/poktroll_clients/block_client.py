from poktroll_clients.ffi import ffi, libpoktroll_clients
from poktroll_clients.go_memory import GoManagedMem, go_ref


class BlockClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, deps_ref: go_ref):
        """
        Constructor for BlockClient.
        :param deps_ref: A Go-managed memory reference to a depinject config.
        """

        go_ref = libpoktroll_clients.NewBlockClient(deps_ref, self.err_ptr)
        super().__init__(go_ref)


class BlockQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    self_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_url: str):
        go_ref = libpoktroll_clients.NewBlockQueryClient(query_node_rpc_url.encode('utf-8'),
                                                         self.err_ptr)

        super().__init__(go_ref)
