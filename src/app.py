#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
        <form action="/echo" method="POST">
            <input type="text" name="user_input">
            <button type="submit">Submit!</button>
        </form>
    '''
@app.route("/echo",methods=['POST'])
def echo():
    input=request.form['user_input']
    return f'''
        Did you type {input}?
    '''


if __name__ == "__main__":
    app.run(debug=True)
