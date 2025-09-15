# app.py
import os

# ⚠️ Hardcoded secret
API_KEY = "12345-super-secret"

# ⚠️ Potential command injection
user_input = input("Enter a filename: ")
os.system(f"cat {user_input}")
