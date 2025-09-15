import os
import pickle
import subprocess
import sqlite3
import hashlib

Weak Hashing
def store_password(password):
    hashed = hashlib.md5(password.encode()).hexdigest()  # 🚩 Weak algorithm
    print("Password stored as:", hashed)

if __name__ == "__main__":
    get_user("admin' OR '1'='1")
    list_files()
    load_data()
    store_password("mypassword")
    ping_host()
