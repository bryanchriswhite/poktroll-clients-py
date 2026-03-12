import pytest
from cffi import FFIError

from poktroll_clients import QueryClient, BlockQueryClient, SupplyMany, RingClient


def get_query_client():
    """Create a QueryClient connected to a running localnet."""
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    deps_ref = SupplyMany(block_query_client)
    return QueryClient("tcp://127.0.0.1:9090", deps_ref)


def test_ring_client_construction():
    """NewRingClient should succeed given a valid QueryClient."""
    query_client = get_query_client()
    ring_client = RingClient(query_client.go_ref)
    assert ring_client.go_ref > 0


def test_ring_client_sign_invalid_relay_request():
    """Signing garbage bytes should raise FFIError (invalid protobuf)."""
    query_client = get_query_client()
    ring_client = RingClient(query_client.go_ref)

    fake_private_key = b"\x00" * 32
    fake_relay_request = b"\xff\xff\xff"

    with pytest.raises(FFIError):
        ring_client.sign_relay_request(fake_private_key, fake_relay_request)


def test_ring_client_sign_empty_session_header():
    """A relay request with no session header should raise FFIError."""
    query_client = get_query_client()
    ring_client = RingClient(query_client.go_ref)

    fake_private_key = b"\x00" * 32
    # Valid-ish protobuf but with empty content (no session header).
    # An empty RelayRequest protobuf is just zero bytes.
    empty_relay_request = b""

    with pytest.raises((FFIError, ValueError)):
        ring_client.sign_relay_request(fake_private_key, empty_relay_request)
