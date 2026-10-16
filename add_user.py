"""Bir kullanıcı ekle ya da var olan kullanıcının parolasını değiştir."""
from getpass import getpass
from pathlib import Path

import yaml
from werkzeug.security import generate_password_hash

users_file = Path(__file__).with_name("users.yml")

username = input("Kullanıcı adı: ").strip()
password = getpass("Parola: ")
if not username or not password:
    raise SystemExit("Kullanıcı adı ve parola boş olamaz.")

with users_file.open("r", encoding="utf-8") as file:
    data = yaml.safe_load(file) or {}

data.setdefault("users", {})[username] = generate_password_hash(password)
with users_file.open("w", encoding="utf-8") as file:
    yaml.safe_dump(data, file, allow_unicode=True, sort_keys=False)

print(f"'{username}' kullanıcısı kaydedildi.")
