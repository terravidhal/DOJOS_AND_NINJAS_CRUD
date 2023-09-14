from flask import Flask
app = Flask(__name__)
#app.secret_key = "7a63b7ac5f8a5640035460f78fc4f8e17dd303eb4b78eeb01c3cd6e53db3b43f" # python -c 'import secrets; print(secrets.token_hex())'