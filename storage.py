import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_file_path(filename):
    path = Path(filename)

    if path.is_absolute():
        return path

    return BASE_DIR / "json_files" / path

def save_users(users, filename):
    path = get_file_path(filename)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def load_users(filename):
    path = get_file_path(filename)
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def safe_load_users(filename):
    try:
        return load_users(filename)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format.")

