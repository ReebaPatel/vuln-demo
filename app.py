import sqlite3
import os
import pickle
import hashlib

# SQL Injection with clearly untrusted input
def get_user_sql():
    username = input("Enter username: ")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Mark input as untrusted explicitly
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")  # SQLi

# Command Injection
def run_command():
    cmd = input("Enter command: ")
    os.system(cmd)  # Command injection

# Weak hash
def weak_hash():
    passwd = input("Enter password: ")
    hashed = hashlib.md5(passwd.encode()).hexdigest()  # Weak hashing

# Insecure deserialization
def insecure_pickle():
    filename = input("Enter pickle file name: ")
    with open(filename, "rb") as f:
        data = pickle.load(f)  # Unsafe deserialization

if __name__ == "__main__":
    get_user_sql()
    run_command()
    weak_hash()
    insecure_pickle()
