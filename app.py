import os
import pickle
import sqlite3

# 1️⃣ Hardcoded secret
SECRET_KEY = "super_secret_password123"  # 🚨 LGTM will flag this

# 2️⃣ SQL Injection
def get_user():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    username = input("Enter username: ")
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")  # 🚨 SQLi
    print(cursor.fetchall())

# 3️⃣ Command Injection
def list_files():
    directory = input("Enter directory to list: ")
    os.system("ls " + directory)  # 🚨 Command Injection

# 4️⃣ Insecure Deserialization
def load_data():
    filename = input("Enter pickle filename: ")
    with open(filename, "rb") as f:
        obj = pickle.load(f)  # 🚨 Insecure deserialization
    print(obj)

if __name__ == "__main__":
    print("=== Vulnerable Demo ===")
    get_user()
    list_files()
    load_data()
