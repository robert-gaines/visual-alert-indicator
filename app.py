from methods import IndicatorMethods
from flask import Flask
import logging
import time
import sys
import os

app = Flask(__name__)

try:
    device = os.getenv('DEVICE')
    model = os.getenv('MODEL')
    key = os.getenv('KEY')
    m = IndicatorMethods(device, model, key)
except Exception as e:
    logging.exception("Failed to instantiate IndicatorMethods")
    sys.exit(1)

@app.route("/red")
def emit_red():
    try:
        m.emit_red()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"

@app.route("/green")
def emit_green():
    try:
        m.emit_green()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"
    
@app.route("/blue")
def emit_blue():
    try:
        m.emit_blue()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"
    
@app.route("/yellow")
def emit_yellow():
    try:
        m.emit_yellow()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"
    
@app.route("/orange")
def emit_orange():
    try:
        m.emit_orange()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"
    
@app.route("/white")
def emit_white():
    try:
        m.emit_white()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"
    
@app.route("/violet")
def emit_violet():
    try:
        m.emit_violet()
        time.sleep(1)
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"

@app.route("/sequence")
def emit_sequence():
    try:
        m.emit_red()
        time.sleep(1)
        m.emit_green()
        time.sleep(1)
        m.emit_blue()
        time.sleep(1)
        m.emit_yellow()
        time.sleep(1)
        m.emit_orange()
        time.sleep(1)
        m.emit_white()
        time.sleep(1)
        m.emit_violet()
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"

@app.route("/duress")
def emit_duress():
    try:
        for i in range(3):
            m.emit_red()
            time.sleep(1)
            m.deactivate_device()
            time.sleep(1)
        for i in range(3):
            m.emit_red()
            time.sleep(3)
            m.deactivate_device()
        for i in range(3):
            m.emit_red()
            time.sleep(1)
            m.deactivate_device()
            time.sleep(1)
        return "200"
    except Exception as e:
        return "400"

@app.route("/activate")
def activate():
    try:
        m.activate_device()
        return "200"
    except Exception as e:
        return "400"
    
@app.route("/deactivate")
def deactivate():
    try:
        m.deactivate_device()
        return "200"
    except Exception as e:
        return "400"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
