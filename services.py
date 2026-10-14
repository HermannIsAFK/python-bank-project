from storage import save_users, safe_load_users

def update_balance(filename, username, amount):
    users = safe_load_users(filename)
    if username in users:
        users[username]["balance"] += amount
        save_users(users, filename)
        return users[username]["balance"]
    else:
        raise ValueError("No such user exists.")
    
