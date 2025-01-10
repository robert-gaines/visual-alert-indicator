
import requests
import logging
import time
import json
import uuid
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

class IndicatorMethods():

    def __init__(self,device,model,key):
        self.model = model
        self.device = device
        self.key = key
        self.headers = {
            "Content-Type": "application/json",
            "Govee-API-Key": self.key
        }
        self.device_control_url = "https://openapi.api.govee.com/router/api/v1/device/control"
        
        try:
            with open('payloads.json', 'r') as f:
                payloads = json.load(f)
        except Exception as e:
            logging.exception(f"Error loading payload configs: {e}")
            sys.exit(1)

        self.deactivate_payload = payloads['deactivate_payload']
        self.activate_payload = payloads['activate_payload']
        self.orange_payload = payloads['orange_payload']
        self.yellow_payload = payloads['yellow_payload']
        self.violet_payload = payloads['violet_payload']
        self.green_payload = payloads['green_payload']
        self.white_payload = payloads['white_payload']
        self.blue_payload = payloads['blue_payload']
        self.red_payload = payloads['red_payload']

    def activate_device(self):
        try:
            self.activate_payload['requestId'] = str(uuid.uuid4())
            self.activate_payload['payload']['sku'] = self.model
            self.activate_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.activate_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Device activated")
            else:
                logging.info("Device activation failed")
        except Exception as e:
            logging.exception(f"Error activating device: {e}")

    def deactivate_device(self):
        try:
            self.deactivate_payload['requestId'] = str(uuid.uuid4())
            self.deactivate_payload['payload']['sku'] = self.model
            self.deactivate_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.deactivate_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Device deactivated")
            else:
                logging.info("Device deactivation failed")
        except Exception as e:  
            logging.exception(f"Error deactivating device: {e}")

    def emit_red(self):
        try:
            self.red_payload['requestId'] = str(uuid.uuid4())
            self.red_payload['payload']['sku'] = self.model
            self.red_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.red_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Red light emitted")
            else:
                logging.info("Red light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting red light: {e}")

    def emit_green(self):
        try:
            self.green_payload['requestId'] = str(uuid.uuid4())
            self.green_payload['payload']['sku'] = self.model
            self.green_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.green_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Green light emitted")
            else:
                logging.info("Green light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting green light: {e}")

    def emit_blue(self):
        try:
            self.blue_payload['requestId'] = str(uuid.uuid4())
            self.blue_payload['payload']['sku'] = self.model
            self.blue_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.blue_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Blue light emitted")
            else:
                logging.info("Blue light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting blue light: {e}")

    def emit_yellow(self):
        try:
            self.yellow_payload['requestId'] = str(uuid.uuid4())
            self.yellow_payload['payload']['sku'] = self.model
            self.yellow_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.yellow_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Yellow light emitted")
            else:
                logging.info("Yellow light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting yellow light: {e}")

    def emit_orange(self):
        try:
            self.orange_payload['requestId'] = str(uuid.uuid4())
            self.orange_payload['payload']['sku'] = self.model
            self.orange_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.orange_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Orange light emitted")
            else:
                logging.info("Orange light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting orange light: {e}")

    def emit_violet(self):
        try:
            self.violet_payload['requestId'] = str(uuid.uuid4())
            self.violet_payload['payload']['sku'] = self.model
            self.violet_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.violet_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("Violet light emitted")
            else:
                logging.info("Violet light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting violet light: {e}")

    def emit_white(self):
        try:
            self.white_payload['requestId'] = str(uuid.uuid4())
            self.white_payload['payload']['sku'] = self.model
            self.white_payload['payload']['device'] = self.device
            response = requests.post(self.device_control_url,
                                    json=self.white_payload, 
                                    headers=self.headers)
            if response.status_code == 200:
                logging.info("White light emitted")
            else:
                logging.info("White light emission failed")
        except Exception as e:
            logging.exception(f"Error emitting white light: {e}")
