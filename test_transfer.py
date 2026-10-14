from storage import save_users, load_users
from services import update_balance, transfer_money
import pytest


def test_successful_transfer(tmp_path):
    path = tmp_path / "users.json"
    
    users = {
        "alice": {
            "balance": 1000
        },
        "bob": {
            "balance": 500
        }
    }
    
    save_users(users, path) 

    result = transfer_money(path, "alice", "bob", 500)

    assert result == {
    "sender_balance": 500,
    "receiver_balance": 1000
    }

    assert load_users(path)["alice"]["balance"] == 500
    assert load_users(path)["bob"]["balance"] == 1000

def test_insufficient_balance(tmp_path):
    path = tmp_path / "users.json"
    
    users = {
        "alice": {
            "balance": 1000
        },
        "bob": {
            "balance": 500
        }
    }
    
    save_users(users, path)

    with pytest.raises(ValueError):
        transfer_money(path, "alice", "bob", 15000)

def test_invalid_amount(tmp_path):
    path = tmp_path / "users.json"
    
    users = {
        "alice": {
            "balance": 1000
        },
        "bob": {
            "balance": 500
        }
    }
    
    save_users(users, path)

    with pytest.raises(ValueError):
        transfer_money(path, "alice", "bob", "one thousand")


def test_missing_receiver(tmp_path):
    path = tmp_path / "users.json"
    
    users = {
        "alice": {
            "balance": 1000
        },
        "bob": {
            "balance": 500
        }
    }
    
    save_users(users, path)

    with pytest.raises(ValueError):
        result = transfer_money(path, "alice", "robert de niro", 1500)