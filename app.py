from flask import Flask, session
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes

if __name__=="__main__":
    app.run(debug=True)