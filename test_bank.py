from storage import save_users, load_users
from services import update_balance
import pytest

def test_deposit(tmp_path):
    path = tmp_path / "users.json"

    users = {
        "alice": {
            "balance": 1000
        }
    }

    save_users(users, path)

    result = update_balance(path, "alice", 500)

    assert result == 1500
    assert load_users(path)["alice"]["balance"] == 1500

def test_withdraw(tmp_path):
    path = tmp_path / "users.json"

    users = {
            "alice": {
                "balance": 1000
            }
        }

    save_users(users, path)

    result = update_balance(path, "alice", -500)

    assert result == 500
    assert load_users(path)["alice"]["balance"] == 500

def test_missing_user(tmp_path):
    path = tmp_path / "users.json"

    with pytest.raises(ValueError):
        update_balance(path, "charlington", 500)