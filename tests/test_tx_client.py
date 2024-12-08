from time import sleep

import pytest
from gen.cosmos.base.v1beta1.coin_pb2 import Coin
from gen.poktroll.gateway.tx_pb2 import MsgStakeGateway, MsgUnstakeGateway
from gen.poktroll.shared.service_pb2 import ApplicationServiceConfig
from gen.poktroll.application.tx_pb2 import MsgStakeApplication, MsgUnstakeApplication, MsgDelegateToGateway
from gen.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from src.block_client import BlockClient, BlockQueryClient
from src.depinject import SupplyMany
from src.events_query_client import EventsQueryClient
from src.go_memory import go_ref
from src.tx_client import TxContext, TxClient


def test_tx_context():
    tx_ctx = TxContext("tcp://127.0.0.1:26657")


def test_tx_client():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "faucet")


@pytest.mark.asyncio
async def test_sign_and_broadcast_success():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "pnf")

    send_msg_from_pnf_to_app3 = MsgSend(
        from_address="pokt1eeeksh2tvkh7wzmfrljnhw4wrhs55lcuvmekkw",
        to_address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex",
        amount=[Coin(denom="upokt", amount="100")]
    )

    try:
        await tx_client.sign_and_broadcast(send_msg_from_pnf_to_app3)
    except Exception as e:
        pytest.fail(f"SignAndBroadcast failed with error: {str(e)}")


@pytest.mark.asyncio
async def test_sign_and_broadcast_many_success():
    cfg_ref = get_tx_client_deps()
    app3_tx_client = TxClient(cfg_ref, "app3")
    gateway2_tx_client = TxClient(cfg_ref, "gateway2")

    app3_addr = "pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex"
    gateway2_addr = "pokt15w3fhfyc0lttv7r585e2ncpf6t2kl9uh8rsnyz"
    gateway_addrs = ["pokt15vzxjqklzjtlz7lahe8z2dfe9nm5vxwwmscne4", gateway2_addr]

    try:
        await gateway2_tx_client.sign_and_broadcast(
            MsgStakeGateway(
                address=gateway2_addr,
                stake=Coin(denom="upokt", amount="111100000")
            )
        )
        sleep(2)

        msgs = [
            MsgStakeApplication(
                address=app3_addr,
                stake=Coin(denom="upokt", amount="222200000"),
                services=[ApplicationServiceConfig(service_id="anvil")]
            ),
            *[MsgDelegateToGateway(
                app_address=app3_addr,
                gateway_address=gateway_addr
            ) for gateway_addr in gateway_addrs],
        ]

        await app3_tx_client.sign_and_broadcast(*msgs)

        await app3_tx_client.sign_and_broadcast(
            MsgUnstakeApplication(address=app3_addr),
        )

        await gateway2_tx_client.sign_and_broadcast(
            MsgUnstakeGateway(address=gateway2_addr)
        )

    except Exception as e:
        pytest.fail(f"SignAndBroadcast failed with error: {str(e)}")


@pytest.mark.asyncio
async def test_sign_and_broadcast_error():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "app1")

    # Attempt to stake an already-staked address (app1)
    stake_app1_msg = MsgStakeApplication(
        address="pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4",
        stake=Coin(denom="upokt", amount="1"),
        services=[ApplicationServiceConfig(service_id="anvil")]
    )

    with pytest.raises(Exception,
                       match=r"(.*failed to execute message.*stake amount.*must be higher than previous stake amount.*|.*EOF: error encountered while querying for tx.*)"):
        await tx_client.sign_and_broadcast(stake_app1_msg)


def get_tx_client_deps() -> go_ref:
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")

    cfg_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(cfg_ref)

    tx_ctx = TxContext("tcp://127.0.0.1:26657")

    return SupplyMany(events_query_client, block_client, tx_ctx)
