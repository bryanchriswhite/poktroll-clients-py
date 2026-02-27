from poktroll_clients import (
    BlockQueryClient,
    Supply,
    Config,
    EventsQueryClient,
)


def test_depinject_supply():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    deps_ref = Supply(client.go_ref)


def test_depinject_supply_many():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")


def test_depinject_config():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    config_ref = Config(events_query_client, block_query_client)
    assert config_ref > 0
