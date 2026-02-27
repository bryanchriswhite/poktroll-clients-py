from typing import Callable

from cffi import FFIError

from poktroll_clients.ffi import ffi, libpoktroll_clients

go_ref = int
callback_type = Callable[[ffi.CData, ffi.CData], None]


def check_err(err_ptr: ffi.CData):
    """Check the FFI error pointer and raise FFIError if an error occurred."""
    if err_ptr[0] != ffi.NULL:
        raise FFIError(ffi.string(err_ptr[0]))


def check_ref(go_ref: go_ref):
    if go_ref < 1:
        raise FFIError("unexpected emtpy go_ref")


class GoManagedMem:
    """
    A base class for all objects which embed Go-managed memory.

    Attributes:
        go_ref: The Go-managed memory reference (int).
    """

    go_ref: go_ref
    err_ptr: ffi.CData = ffi.new("char **")

    def __init__(self, go_ref: go_ref):
        """
        Constructor for GoManagedMem. Stores the Go-managed memory reference.
        """

        self.go_ref = go_ref

        check_err(self.err_ptr)
        check_ref(go_ref)

    def __del__(self):
        """
        Destructor for GoManagedMem. Frees the Go-managed memory associated with the reference.
        """

        libpoktroll_clients.FreeGoMem(self.go_ref)
