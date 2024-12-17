from pprint import pprint

import pytest

from poktroll_clients.proto.poktroll.shared.params_pb2 import Params as SharedParams
from poktroll_clients.query_client import QueryClient


# @pytest.mark.asyncio
def test_query_client():
    query_client = QueryClient("http://127.0.0.1:26657")

    # shared_params = await query_client.get_shared_params()
    shared_params = query_client.get_shared_params()

    expected_shared_params = SharedParams(
        num_blocks_per_session=10,
        grace_period_end_offset_blocks=1,
        claim_window_open_offset_blocks=1,
        claim_window_close_offset_blocks=4,
        proof_window_close_offset_blocks=4,
        supplier_unbonding_period_sessions=1,
        application_unbonding_period_sessions=1,
        compute_units_to_tokens_multiplier=42,
    )

    assert shared_params == expected_shared_params
