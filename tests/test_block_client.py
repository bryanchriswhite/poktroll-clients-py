from poktroll_clients import (
    BlockQueryClient,
    BlockClient,
    EventsQueryClient,
    SupplyMany,
)


def test_block_query_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")


def test_block_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    deps_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(deps_ref)


def test_block_query_client_block():
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    # Query latest block (no height specified)
    result = block_query_client.block()
    assert result > 0

def test_block_query_client_block_at_height():
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    # Query block at specific height
    result = block_query_client.block(height=1)
    assert result > 0
