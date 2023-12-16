import logging
import time

import requests


class Clash:
    @staticmethod
    def rule_mode():
        Clash.send_request('Rule')
        logging.info('Switch to Rule Mode')
        time.sleep(0.5)

    @staticmethod
    def global_mode():
        Clash.send_request('Global')
        logging.info('Switch to Global Mode')
        time.sleep(0.5)

    @staticmethod
    def send_request(mode: str):
        secret = '5a6675ec-1201-4596-9469-6b2c2808b956'
        header = {'Authorization': f'Bearer {secret}'}
        body = {'mode': mode}
        res = requests.session().request(headers=header, method='patch', url='http://127.0.0.1:61425/configs',
                                         json=body)
