import os
import pickle
import subprocess
import sqlite3
import hashlib

# ⚠️ 1. Hardcoded secret
SECRET_KEY = "super_secret_password123"

# ⚠️ 2. SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # 🚩 Directly injecting user input
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    print(cursor.fetchall())

# ⚠️ 3. Command Injection
def list_files():
    user_input = input("Enter directory to list: ")
    os.system(f"ls {user_input}")

# ⚠️ 4. Insecure Deserialization
def load_data():
    with open("data.pkl", "rb") as f:
        obj = pickle.load(f)  # 🚩 No validation

# ⚠️ 5. Weak Hashing
def store_password(password):
    hashed = hashlib.md5(password.encode()).hexdigest()  # 🚩 Weak algorithm
    print("Password stored as:", hashed)

# ⚠️ 6. Unsafe subprocess
def ping_host():
    host = input("Enter host to ping: ")
    subprocess.call("ping " + host, shell=True)

if __name__ == "__main__":
    get_user("admin' OR '1'='1")
    list_files()
    load_data()
    store_password("mypassword")
    ping_host()
