import logging
import time

import requests


class Clash:
    @staticmethod
    def rule_mode():
        Clash.send_change_proxy_mode_request('Rule')

    @staticmethod
    def global_mode():
        Clash.send_change_proxy_mode_request('Global')

    @staticmethod
    def send_change_proxy_mode_request(mode: str):
        secret = '5a6675ec-1201-4596-9469-6b2c2808b956'
        header = {'Authorization': f'Bearer {secret}'}
        body = {'mode': mode}
        res = requests.session().request(headers=header, method='patch', url='http://127.0.0.1:61425/configs',
                                         json=body)
        time.sleep(0.5)
        logging.info(f'Switch to {mode} Mode')
