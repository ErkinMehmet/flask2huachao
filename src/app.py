#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
        <form action="/echo_user_input" method="POST">
            <input type="text" name="user_input">
            <button type="submit">Submit!</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
