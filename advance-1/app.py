import os
from flask import Flask
app = Flask(_name_)

@app.route("/")
def main():
    return "Welcome"

@app.route('/how are you')
def hello():
    return 'I am good. How about you?'

if __name__ == "__main__":
    app.run()