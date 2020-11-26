import os
import re
import logging
import requests


class MacSearch:
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', \
                            level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        self.base_url = "https://api.macaddress.io/v1?output=vendor"

    def mac_search(self, mac_address):
        try:
            logging.info("Looking for MAC address {}".format(mac_address))
            payload = {}
            params = {'search': mac_address}
            api_key = os.environ.get('MAC_ADDRESS_IO_API_KEY')
            headers = {
                'X-Authentication-Token': api_key
            }
            if self.is_valid_mac_address(mac_address):
                response = requests.request("GET", self.base_url, headers=headers, data=payload, params=params)
                response.raise_for_status()
                if response and response.text:
                    print("Company Name associated with the MAC address : {}".format(response.text))
                else:
                    logging.info("MAC address {} not found".format(mac_address))
            else:
                logging.error("Please enter a valid MAC Address")
                return
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.ConnectionError as errc:
            logging.error("Error Connecting : {}".format(errc))
        except requests.exceptions.Timeout as errt:
            logging.error("Timeout Error : {}".format(errt))
        except requests.exceptions.RequestException as err:
            logging.error("Failed to lookup the MAC address {}:{}".format(mac_address, err))

    # Function to validate MAC address
    def is_valid_mac_address(self, mac_add):
        regex = ("^([0-9A-Fa-f]{2}[:-])" +
                 "{5}([0-9A-Fa-f]{2})|" +
                 "([0-9a-fA-F]{4}\\." +
                 "[0-9a-fA-F]{4}\\." +
                 "[0-9a-fA-F]{4})$")

        match = re.compile(regex)
        if mac_add is None:
            return False
        if re.search(match, mac_add):
            return True
        return False
