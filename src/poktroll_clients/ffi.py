import platform
from ctypes.util import find_library
from os import path, environ
from pathlib import Path
from typing import Callable, Tuple

from cffi import FFI

# Initialize CFFI
ffi = FFI()

callback_type = Callable[[ffi.CData, ffi.CData], None]

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# TODO_IMPROVE: Extract docstring to an appropriately named file.
# DEV_NOTE: ffi.cdef MUST NOT depend on any pre-processing (e.g. macros, defs, etc.).

# Determine pthread struct sizes based on platform
_system = platform.system()
_machine = platform.machine()

if _system == "Darwin":
    _PTHREAD_MUTEX_SIZE = 64
    _PTHREAD_COND_SIZE = 48
    _PTHREAD_ALIGN_TYPE = "long int"
elif _system == "Linux" and _machine == "aarch64":
    _PTHREAD_MUTEX_SIZE = 48
    _PTHREAD_COND_SIZE = 48
    _PTHREAD_ALIGN_TYPE = "long int"
else:  # Linux x86_64 and others
    _PTHREAD_MUTEX_SIZE = 40
    _PTHREAD_COND_SIZE = 48
    _PTHREAD_ALIGN_TYPE = "long int"

ffi.cdef(f"""
    typedef struct {{
        unsigned char __size[{_PTHREAD_MUTEX_SIZE}];
        {_PTHREAD_ALIGN_TYPE} __align;
    }} pthread_mutex_t;

    typedef struct {{
        unsigned char __size[{_PTHREAD_COND_SIZE}];
        long long int __align;
    }} pthread_cond_t;

    typedef struct AsyncContext {{
        pthread_mutex_t mutex;
        pthread_cond_t cond;
        bool completed;
        bool success;
        void* data;
        size_t data_len;
        int error_code;
        char error_msg[256];
    }} AsyncContext;

    typedef void (*success_callback)(AsyncContext* ctx, const void* result);
    typedef void (*error_callback)(AsyncContext* ctx, const char* error);
    typedef void (*cleanup_callback)(AsyncContext* ctx);

    typedef struct AsyncOperation {{
        AsyncContext* ctx;
        success_callback on_success;
        error_callback on_error;
        cleanup_callback cleanup;
    }} AsyncOperation;

    void init_context(AsyncContext* ctx);
    void cleanup_context(AsyncContext* ctx);
    void handle_error(AsyncContext* ctx, const char* error);
    void handle_success(AsyncContext* ctx, const void* result);
    bool wait_for_completion(AsyncContext* ctx, int timeout_ms);

    typedef void (callback_fn)(void *data, char **err);

    typedef int64_t go_ref;

    void FreeGoMem(go_ref ref);

    /* ── depinject ── */
    go_ref Supply(go_ref goRef, char** cErr);
    go_ref SupplyMany(go_ref* goRefs, int numGoRefs, char** cErr);
    go_ref Config(go_ref* goRefs, int numGoRefs, char** cErr);

    /* ── protobuf ── */
    typedef struct {{
        uint8_t* type_url;
        size_t type_url_length;
        uint8_t* data;
        size_t data_length;
    }} serialized_proto;

    typedef struct {{
        serialized_proto* protos;
        size_t num_protos;
    }} serialized_proto_array;

    void* GetGoProtoAsSerializedProto(go_ref ref, char** cErr);

    /* ── gas ── */
    typedef struct gas_settings {{
        uint64_t gas_limit;
        bool simulate;
        char *gas_prices;
        double gas_adjustment;
        char *fees;
    }} gas_settings;

    /* ── morse keys ── */
    typedef uint8_t morse_signature[64];

    /* ── block client ── */
    go_ref NewBlockClient(go_ref depsRef, char** cErr);

    /* ── block query client ── */
    go_ref NewBlockQueryClient(char* cometWebsocketURL, char** cErr);
    go_ref BlockQueryClient_Block(go_ref clientRef, int64_t* cHeight, char** cErr);

    /* ── tx context ── */
    go_ref NewTxContext(char* tcpURL, char** cErr);

    /* ── tx client ── */
    go_ref NewTxClient(go_ref depsRef, char* signingKeyName, gas_settings* gasSetting, char** cErr);
    go_ref WithSigningKeyName(char* keyName);
    go_ref TxClient_SignAndBroadcast(AsyncOperation* op, go_ref txClientRef, serialized_proto* serializedProto);
    go_ref TxClient_SignAndBroadcastMany(AsyncOperation* op, go_ref txClientRef, serialized_proto_array* serializedProtoArray);

    /* ── query client ── */
    go_ref NewQueryClient(go_ref depsRef, char* queryNodeRPCURL, char** cErr);
    void* QueryClient_GetSessionParams(go_ref clientRef, char** cErr);
    void* QueryClient_GetProofParams(go_ref clientRef, char** cErr);
    void* QueryClient_GetMigrationParams(go_ref clientRef, char** cErr);
    void* QueryClient_GetMorseClaimableAccounts(go_ref clientRef, char** cErr);
    void* QueryClient_GetMorseClaimableAccount(go_ref clientRef, char* cMorseSrcAddress, char** cErr);

    /* ── app query client ── */
    void* QueryClient_GetApplication(go_ref clientRef, char* appAddress, char** cErr);
    void* QueryClient_GetAllApplications(go_ref clientRef, char** cErr);

    /* ── service query client ── */
    void* QueryClient_GetService(go_ref clientRef, char* serviceId, char** cErr);
    void* QueryClient_GetServiceRelayDifficulty(go_ref clientRef, char* serviceId, char** cErr);

    /* ── session query client ── */
    void* QueryClient_GetSession(go_ref clientRef, char* appAddress, char* serviceId, int64_t blockHeight, char** cErr);

    /* ── shared query client ── */
    void* QueryClient_GetSharedParams(go_ref depsRef, char** cErr);
    int64_t QueryClient_GetSessionGracePeriodEndHeight(go_ref depsRef, int64_t queryHeight, char** cErr);
    int64_t QueryClient_GetClaimWindowOpenHeight(go_ref depsRef, int64_t queryHeight, char** cErr);
    int64_t QueryClient_GetEarliestSupplierClaimCommitHeight(go_ref clientRef, int64_t queryHeight, char* supplierOperatorAddr, char** cErr);
    int64_t QueryClient_GetProofWindowOpenHeight(go_ref clientRef, int64_t queryHeight, char** cErr);
    int64_t QueryClient_GetEarliestSupplierProofCommitHeight(go_ref clientRef, int64_t queryHeight, char* supplierOperatorAddr, char** cErr);
    uint64_t QueryClient_GetComputeUnitsToTokensMultiplier(go_ref clientRef, char** cErr);

    /* ── supplier query client ── */
    void* QueryClient_GetSupplier(go_ref clientRef, char* supplierAddress, char** cErr);
    void* QueryClient_GetAllSuppliers(go_ref clientRef, char** cErr);

    /* ── morse claim messages ── */
    go_ref LoadMorsePrivateKey(char* morseKeyExportPath, char* passphrase, char** cErr);
    void* NewSerializedSignedMsgClaimMorseAccount(char* cShannonDestAddr, go_ref privKeyRef, char* cShannonSigningAddr, char** cErr);
    void* NewSerializedSignedMsgClaimMorseApplication(char* cShannonDestAddr, go_ref privKeyRef, char* serviceId, char* cShannonSigningAddr, char** cErr);
    void* NewSerializedSignedMsgClaimMorseSupplier(char* cShannonOwnerAddr, char* cShannonOperatorAddr, char* cMorseNodeAddr, go_ref privKeyRef, serialized_proto_array* cSupplierServiceConfigs, char* cShannonSigningAddr, char** cErr);
    char* GetMorseAddress(go_ref privKeyRef, char** cErr);
    void SignMorseClaimMsg(serialized_proto* cSerializedProto, go_ref privKeyRef, uint8_t* cOutMorseSignature, char** cErr);

    /* ── ring client ── */
    go_ref NewRingClient(go_ref queryClientRef, char** cErr);
    void RingClient_SignRelayRequest(go_ref ringClientRef, uint8_t* cPrivKeyBz, size_t cPrivKeyBzLen, uint8_t* cRelayRequestBz, size_t cRelayRequestBzLen, uint8_t** cOutSigBz, size_t* cOutSigBzLen, char** cErr);
    void FreeCBytes(uint8_t* cBz);
""")


def get_platform_info() -> Tuple[str, str]:
    """
    Get exact OS and architecture information.

    Returns:
        Tuple of (os_name, machine) exactly as reported by platform module
    """
    system = platform.system()
    machine = platform.machine()

    # Validate system
    if system not in ("Linux", "Darwin", "Windows"):
        raise OSError(f"Unsupported operating system: {system}")

    # Validate machine architecture
    valid_machines = {
        "Linux": {"x86_64", "aarch64"},
        "Darwin": {"x86_64", "arm64"},
        "Windows": {"AMD64", "x86"}
    }

    if machine not in valid_machines[system]:
        raise OSError(
            f"Unsupported architecture {machine} for {system}. "
            f"Supported architectures: {valid_machines[system]}"
        )

    return system, machine


def machine_to_go_arch(machine: str) -> str:
    """Map platform.machine() values to Go architecture names."""

    arch_map = {
        "x86_64": "amd64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }

    return arch_map[machine]


def get_packaged_library_name(system: str, machine: str) -> str:
    """
    Get the exact platform-specific library name.

    Args:
        system: Value from platform.system()
        machine: Value from platform.machine()

    Returns:
        The platform-specific library filename
    """

    go_arch = machine_to_go_arch(machine)

    if system == "Linux":
        return f"libpoktroll_clients-{go_arch}.so"
    elif system == "Darwin":
        return f"libpoktroll_clients-{go_arch}.dylib"
    elif system == "Windows":
        return f"poktroll_clients-{go_arch}.dll"
    else:
        raise OSError(f"Unsupported platform combination: {system} {machine}")


def get_packaged_library_path() -> Path:
    """
    Get the full path to the appropriate packaged native library for the current platform.

    Returns:
        Path to the native library

    Raises:
        OSError: If the platform is unsupported or the library is not found
    """

    system, machine = get_platform_info()
    lib_name = get_packaged_library_name(system, machine)

    package_dir = Path(__file__).parent.absolute()
    lib_path = package_dir / 'lib' / lib_name

    if not lib_path.exists():
        raise OSError(
            f"Native library not found for {system} {machine}\n"
            f"Expected path: {lib_path}\n"
            f"Expected filename: {lib_name}"
        )

    return lib_path


lib_dir = path.join(path.dirname(path.abspath(__file__)), "lib")
_platform_system = platform.system()
if _platform_system == "Darwin":
    lib_path_var = "DYLD_LIBRARY_PATH"
elif _platform_system == "Windows":
    lib_path_var = "PATH"
else:
    lib_path_var = "LD_LIBRARY_PATH"

# Prepend the library directory to the "library path" environment variable for highest precedence.
environ[lib_path_var] = f"{lib_dir}:{environ.get(lib_path_var, '')}"

# print(f"lib_path_var: {lib_path_var}; lib_dir: {lib_dir}")
# print(f"env: {environ[lib_path_var]}")

lib_load_path = find_library("poktroll_clients")
if lib_load_path is None:
    lib_load_path = get_packaged_library_path()

print(f"Loading shared library from: {lib_load_path}")

# Load the shared library.
libpoktroll_clients = ffi.dlopen(str(lib_load_path))

# TODO_UP_NEXT: select shared library based on OS/Arch.
# libpoktroll_clients = ffi.dlopen(str(get_library_path()))
# TODO_UP_NEXT: add env var to add include directory with OS installed version.
# TODO_CONSIDERATION: look for an OS installed shared library if there's no packaged one for the current OS/Arch.
