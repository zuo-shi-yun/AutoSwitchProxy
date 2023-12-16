from pkg.plugin.host import EventContext, PluginHost
from pkg.plugin.models import *
from plugins.AutoSwitchProxy.utils.clash import Clash

"""
自动更换cfw的proxy模式
"""


# 注册插件
@register(name="AutoSwitchProxy", description="自动更换cfw的proxy模式", version="1.0", author="zuoShiYun")
class AutoSwitchProxy(Plugin):
    def __init__(self, plugin_host: PluginHost):
        self.host = plugin_host

    @on(PersonNormalMessageReceived)
    @on(GroupNormalMessageReceived)
    def handle_normal_msg_send(self, event: EventContext, **kwargs):
        Clash.global_mode()  # 更改cfw模式——global

    @on(NormalMessageResponded)
    def handle_normal_msg_sent(self, event: EventContext, **kwargs):
        Clash.rule_mode()  # 更改cfw模式——rule

    # 插件卸载时触发
    def __del__(self):
        pass


if __name__ == 'main':
    pass
