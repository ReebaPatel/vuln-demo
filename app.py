from flask import Flask, request
import sqlite3
import os
import pickle
import hashlib

app = Flask(__name__)

# 1️⃣ Hardcoded secret
SECRET_KEY = "super_secret_password123"  # 🚨 Hardcoded secret

# Initialize DB
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT,
                        password TEXT
                      )''')
    conn.commit()
    conn.close()

init_db()

# 2️⃣ SQL Injection
@app.route("/login")
def login():
    username = request.args.get("username")  # user-controlled input
    password = request.args.get("password")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # 🚨 SQL Injection
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    return str(cursor.fetchall())

# 3️⃣ Command Injection
@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")  # user-controlled input
    os.system(cmd)  # 🚨 Command injection
    return "Command executed!"

# 4️⃣ Weak hashing
@app.route("/register")
def register():
    username = request.args.get("username")
    password = request.args.get("password")
    hashed = hashlib.md5(password.encode()).hexdigest()  # 🚨 Weak hashing
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users VALUES ('{username}','{hashed}')")
    conn.commit()
    return "User registered!"

# 5️⃣ Insecure deserialization
@app.route("/load_pickle")
def load_pickle():
    filename = request.args.get("file")
    with open(filename, "rb") as f:
        data = pickle.load(f)  # 🚨 Insecure deserialization
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)
