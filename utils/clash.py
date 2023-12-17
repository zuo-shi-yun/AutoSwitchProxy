import logging
import os
import platform
import time

import requests
from ruamel.yaml import YAML

# API地址
external_controller = None
# API密钥 若为空请改为''
secret = None


class Clash:
    @classmethod
    def rule_mode(cls):
        cls.send_change_proxy_mode_request('Rule')

    @classmethod
    def global_mode(cls):
        cls.send_change_proxy_mode_request('Global')

    @classmethod
    def get_api_config(cls):
        system = platform.system()

        if system != "Windows":
            raise Exception('自动导入配置仅支持windows系统,请手动设置clash配置')

        user_name = os.environ.get("USERNAME")  # 用户名
        # 配置文件路径
        config_path = fr"C:\Users\{user_name}\.config\clash\config.yml"

        # 配置文件yaml
        try:
            with open(config_path, 'r', encoding='utf-8') as f:  # 读
                yamls = YAML(typ='rt')
                config = yamls.load(f)
        except Exception as e:
            raise Exception(f'读取{config_path}文件失败,请检查文件是否存在或是否具有读取权限')

        # 检查配置项
        if 'external-controller' not in config:
            raise Exception(f'{config_path}文件中未找到external-controller配置项,请更改配置文件或手动配置')
        if 'secret' not in config:
            raise Exception(f'{config_path}文件中未找到secret配置项,请更改配置文件或手动配置')

        # 导入配置
        global external_controller, secret
        external_controller = config['external-controller']
        secret = config['secret']
        logging.info('clash配置导入成功')

    @classmethod
    def check_clash_api_connect(cls):
        try:
            res = requests.get(f'http://{external_controller}/configs')
            logging.info('clash api连接正常')
        except Exception as e:
            raise Exception(
                f'clash api连接失败,请检查clash 配置是否正确.当前配置:external-controller:{external_controller},secret:{secret}')

    @staticmethod
    def send_change_proxy_mode_request(mode: str):
        global external_controller, secret
        header = {'Authorization': f'Bearer {secret}'}
        body = {'mode': mode}
        res = requests.session().request(headers=header, method='patch', url=f'http://{external_controller}/configs',
                                         json=body)

        time.sleep(0.5)

        logging.info(f'Switch to {mode} Mode')
