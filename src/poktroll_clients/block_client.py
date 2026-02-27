from poktroll_clients.ffi import ffi, libpoktroll_clients
from poktroll_clients.go_memory import GoManagedMem, go_ref, check_err, check_ref


class BlockClient(GoManagedMem):
    """Subscribes to new blocks from a CometBFT node."""

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
    """Queries block information from a CometBFT node."""

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_url: str):
        go_ref = libpoktroll_clients.NewBlockQueryClient(query_node_rpc_url.encode('utf-8'),
                                                         self.err_ptr)
        super().__init__(go_ref)

    def block(self, height: int = None) -> go_ref:
        """
        Query a block by height.
        :param height: Block height to query. If None, returns the latest block.
        :return: A go_ref to the block result.
        """
        err_ptr = ffi.new("char **")
        if height is not None:
            c_height = ffi.new("int64_t *", height)
        else:
            c_height = ffi.NULL
        ref = libpoktroll_clients.BlockQueryClient_Block(self.go_ref, c_height, err_ptr)
        check_err(err_ptr)
        check_ref(ref)
        return ref
