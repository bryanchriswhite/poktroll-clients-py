from typing import List

from cffi import FFIError

from poktroll_clients.ffi import ffi, libpoktroll_clients
from poktroll_clients.go_memory import GoManagedMem, go_ref, check_err, check_ref
from poktroll_clients.protobuf import deserialize_proto, deserialize_proto_array

from poktroll_clients.proto.pocket.session import params_pb2 as session_params_pb2
from poktroll_clients.proto.pocket.proof import params_pb2 as proof_params_pb2
from poktroll_clients.proto.pocket.shared import params_pb2 as shared_params_pb2
from poktroll_clients.proto.pocket.migration import params_pb2 as migration_params_pb2
from poktroll_clients.proto.pocket.migration import morse_onchain_pb2
from poktroll_clients.proto.pocket.application import types_pb2 as application_types_pb2
from poktroll_clients.proto.pocket.shared import service_pb2
from poktroll_clients.proto.pocket.service import relay_mining_difficulty_pb2
from poktroll_clients.proto.pocket.session import types_pb2 as session_types_pb2
from poktroll_clients.proto.pocket.shared import supplier_pb2


class QueryClient(GoManagedMem):
    """
    Python wrapper for the poktroll MultiQueryClient.
    Provides query access to all on-chain module params and state.
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_url: str, deps_ref: go_ref = -1):
        """
        Constructor for QueryClient.
        :param query_node_rpc_url: The gRPC query URL (e.g. "tcp://127.0.0.1:9090").
        :param deps_ref: Optional depinject config go_ref. If not provided, a default config is used.
        """
        err_ptr = ffi.new("char **")
        ref = libpoktroll_clients.NewQueryClient(
            deps_ref,
            query_node_rpc_url.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        super().__init__(ref)

    # -- Params queries --

    def get_session_params(self) -> session_params_pb2.Params:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetSessionParams(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, session_params_pb2.Params)

    def get_proof_params(self) -> proof_params_pb2.Params:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetProofParams(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, proof_params_pb2.Params)

    def get_shared_params(self) -> shared_params_pb2.Params:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetSharedParams(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, shared_params_pb2.Params)

    def get_migration_params(self) -> migration_params_pb2.Params:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetMigrationParams(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, migration_params_pb2.Params)

    # -- Morse migration queries --

    def get_morse_claimable_accounts(self) -> List[morse_onchain_pb2.MorseClaimableAccount]:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetMorseClaimableAccounts(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto_array(raw_ptr, morse_onchain_pb2.MorseClaimableAccount)

    def get_morse_claimable_account(self, morse_src_address: str) -> morse_onchain_pb2.MorseClaimableAccount:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetMorseClaimableAccount(
            self.go_ref,
            morse_src_address.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, morse_onchain_pb2.MorseClaimableAccount)

    # -- Application queries --

    def get_application(self, app_address: str) -> application_types_pb2.Application:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetApplication(
            self.go_ref,
            app_address.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, application_types_pb2.Application)

    def get_all_applications(self) -> List[application_types_pb2.Application]:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetAllApplications(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto_array(raw_ptr, application_types_pb2.Application)

    # -- Service queries --

    def get_service(self, service_id: str) -> service_pb2.Service:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetService(
            self.go_ref,
            service_id.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, service_pb2.Service)

    def get_service_relay_difficulty(self, service_id: str) -> relay_mining_difficulty_pb2.RelayMiningDifficulty:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetServiceRelayDifficulty(
            self.go_ref,
            service_id.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, relay_mining_difficulty_pb2.RelayMiningDifficulty)

    # -- Session queries --

    def get_session(self, app_address: str, service_id: str, block_height: int = 0) -> session_types_pb2.Session:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetSession(
            self.go_ref,
            app_address.encode('utf-8'),
            service_id.encode('utf-8'),
            block_height,
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, session_types_pb2.Session)

    # -- Shared module queries --

    def get_session_grace_period_end_height(self, query_height: int) -> int:
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.QueryClient_GetSessionGracePeriodEndHeight(
            self.go_ref, query_height, err_ptr,
        )
        check_err(err_ptr)
        return result

    def get_claim_window_open_height(self, query_height: int) -> int:
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.QueryClient_GetClaimWindowOpenHeight(
            self.go_ref, query_height, err_ptr,
        )
        check_err(err_ptr)
        return result

    def get_earliest_supplier_claim_commit_height(self, query_height: int, supplier_operator_addr: str) -> int:
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.QueryClient_GetEarliestSupplierClaimCommitHeight(
            self.go_ref, query_height, supplier_operator_addr.encode('utf-8'), err_ptr,
        )
        check_err(err_ptr)
        return result

    def get_proof_window_open_height(self, query_height: int) -> int:
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.QueryClient_GetProofWindowOpenHeight(
            self.go_ref, query_height, err_ptr,
        )
        check_err(err_ptr)
        return result

    def get_earliest_supplier_proof_commit_height(self, query_height: int, supplier_operator_addr: str) -> int:
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.QueryClient_GetEarliestSupplierProofCommitHeight(
            self.go_ref, query_height, supplier_operator_addr.encode('utf-8'), err_ptr,
        )
        check_err(err_ptr)
        return result

    def get_compute_units_to_tokens_multiplier(self) -> int:
        err_ptr = ffi.new("char **")
        result = libpoktroll_clients.QueryClient_GetComputeUnitsToTokensMultiplier(
            self.go_ref, err_ptr,
        )
        check_err(err_ptr)
        return result

    # -- Supplier queries --

    def get_supplier(self, supplier_address: str) -> supplier_pb2.Supplier:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetSupplier(
            self.go_ref,
            supplier_address.encode('utf-8'),
            err_ptr,
        )
        check_err(err_ptr)
        return deserialize_proto(raw_ptr, supplier_pb2.Supplier)

    def get_all_suppliers(self) -> List[supplier_pb2.Supplier]:
        err_ptr = ffi.new("char **")
        raw_ptr = libpoktroll_clients.QueryClient_GetAllSuppliers(self.go_ref, err_ptr)
        check_err(err_ptr)
        return deserialize_proto_array(raw_ptr, supplier_pb2.Supplier)
