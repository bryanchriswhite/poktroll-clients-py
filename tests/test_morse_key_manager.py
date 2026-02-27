import pytest
from poktroll_clients import MorseKeyManager


@pytest.mark.skip(reason="Requires Morse key export file")
def test_morse_key_manager_load():
    """Test loading a Morse private key from an export file."""
    manager = MorseKeyManager("/path/to/morse/key/export.json", "passphrase")
    assert manager.go_ref > 0


@pytest.mark.skip(reason="Requires Morse key export file")
def test_morse_address():
    """Test deriving Morse address from loaded key."""
    manager = MorseKeyManager("/path/to/morse/key/export.json", "passphrase")
    address = manager.morse_address
    assert isinstance(address, str)
    assert len(address) > 0


@pytest.mark.skip(reason="Requires Morse key export file and running node")
def test_new_msg_claim_morse_account():
    """Test creating a signed MsgClaimMorseAccount."""
    manager = MorseKeyManager("/path/to/morse/key/export.json", "passphrase")
    msg = manager.new_msg_claim_morse_account(
        shannon_dest_addr="pokt1test...",
        shannon_signing_addr="pokt1test...",
    )
    assert msg is not None
    assert len(msg.morse_public_key) > 0
    assert len(msg.morse_signature) > 0
