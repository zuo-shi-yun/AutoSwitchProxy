from pkg.plugin.host import EventContext, PluginHost
from pkg.plugin.models import *
from plugins.AutoSwitchProxy.utils.clash import Clash, external_controller, secret

"""
自动更换cfw的proxy模式
"""


# 注册插件
@register(name="AutoSwitchProxy", description="自动更换cfw的proxy模式", version="1.0", author="zuoShiYun")
class AutoSwitchProxy(Plugin):
    def __init__(self, plugin_host: PluginHost):
        self.host = plugin_host
        get_config()  # 获得配置
        Clash.rule_mode()  # 默认rule模式

    @on(PersonNormalMessageReceived)
    @on(GroupNormalMessageReceived)
    def handle_normal_msg_send(self, event: EventContext, **kwargs):
        Clash.global_mode()  # 更改cfw模式——global

    @on(NormalMessageResponded)
    @on(SessionExpired)
    def handle_normal_msg_sent(self, event: EventContext, **kwargs):
        Clash.rule_mode()  # 更改cfw模式——rule

    # 插件卸载时触发
    def __del__(self):
        pass


# 获得clash配置
def get_config():
    if isinstance(external_controller, str) and isinstance(secret, str):
        logging.info("自定义clash配置")
    elif isinstance(external_controller, str):
        raise Exception('仅手动配置了external_controller,请同时配置secret')
    elif isinstance(secret, str):
        raise Exception('仅手动配置了secret,请同时配置external_controller')
    else:
        logging.info("自动获取clash配置")
        Clash.get_api_config()
    # 检查配置项
    Clash.check_clash_api_connect()


if __name__ == 'main':
    pass
