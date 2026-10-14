from storage import save_users, safe_load_users

def update_balance(filename, username, amount):
    users = safe_load_users(filename)
    if username in users:
        users[username]["balance"] += amount
        save_users(users, filename)
        return users[username]["balance"]
    else:
        raise ValueError("No such user exists.")
    
def transfer_money(filename, sender, receiver, amount):
    users = safe_load_users(filename)
    if sender not in users:
        raise ValueError("No such user (sender) exist.")
    if receiver not in users:
        raise ValueError("No such user (receiver) exist.")
    if (type(amount) != int and type(amount) != float) or amount <= 0:
        raise ValueError("Incorrect amount.")
    if users[sender]["balance"] <= amount:
        raise ValueError("Insufficient balance.")
    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    save_users(users, filename)
    return {"sender_balance": users[sender]["balance"], "receiver_balance": users[receiver]["balance"]}