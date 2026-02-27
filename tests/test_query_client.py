import pytest
from poktroll_clients import QueryClient, EventsQueryClient, BlockQueryClient, SupplyMany


def get_query_client_deps():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    return SupplyMany(events_query_client, block_query_client)


def test_query_client():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    assert query_client.go_ref > 0


def test_get_shared_params():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    params = query_client.get_shared_params()
    assert params is not None


def test_get_session_params():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    params = query_client.get_session_params()
    assert params is not None


def test_get_proof_params():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    params = query_client.get_proof_params()
    assert params is not None


def test_get_all_applications():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    apps = query_client.get_all_applications()
    assert isinstance(apps, list)


def test_get_all_suppliers():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    suppliers = query_client.get_all_suppliers()
    assert isinstance(suppliers, list)


def test_get_compute_units_to_tokens_multiplier():
    deps_ref = get_query_client_deps()
    query_client = QueryClient("tcp://127.0.0.1:9090", deps_ref)
    multiplier = query_client.get_compute_units_to_tokens_multiplier()
    assert multiplier > 0
