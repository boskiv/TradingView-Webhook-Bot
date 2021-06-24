# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : main.py                 #
# ----------------------------------------------- #

import json
import os
import time

from flask import Flask, request
import logging
import config
from handler import *
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            if key == config.sec_key:
                logging.info("Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200

            else:
                logging.error('Alert Received & Refused! (Wrong Key)')
                return "Refused alert", 400

    except Exception as e:
        logging.error("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=os.environ("PORT", 80))
