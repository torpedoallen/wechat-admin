# coding=utf8

from flask import Flask, request
app = Flask(__name__)


def index():
    echostr = request.args.get('echostr', '')
    return echostr

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998)
