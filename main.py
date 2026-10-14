# from services import update_balance

# new_balance = update_balance("bank_users.json", "charlie", 500)

# print(new_balance)

from pathlib import Path
from storage import save_users, load_users

test_path = Path("/tmp/bank_test.json")

save_users({"alice": {"balance": 100}}, test_path)

print(load_users(test_path))