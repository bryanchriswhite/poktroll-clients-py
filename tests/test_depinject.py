from poktroll_clients import (
    BlockQueryClient,
    Supply,
    Config,
)


def test_depinject_supply():
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    deps_ref = Supply(block_query_client.go_ref)


def test_depinject_supply_many():
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")


def test_depinject_config():
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    config_ref = Config(block_query_client)
    assert config_ref > 0
