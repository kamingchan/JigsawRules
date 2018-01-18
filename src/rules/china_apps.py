from rules.rules import Rules


class Tencent(Rules):
    def __str__(self):
        return '''# Rule for WeChat
USER-AGENT,TencentConnect,{proxy_group}
USER-AGENT,WiFi%E7%AE%A1%E5%AE%B6/*,{proxy_group}
USER-AGENT,TIM/*,{proxy_group}
USER-AGENT,MicroMessenger Client,{proxy_group}
USER-AGENT,WeChat/*,{proxy_group}
DOMAIN-SUFFIX,qpic.cn,{proxy_group}
DOMAIN-SUFFIX,qq.com,{proxy_group}
DOMAIN-SUFFIX,weixinbridge.com,{proxy_group}
DOMAIN-SUFFIX,servicewechat.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )


class Alibaba(Rules):
    def __str__(self):
        return '''# Rule for Alibaba Apps
USER-AGENT,%E6%94%AF%E4%BB%98%E5%AF%B6/*,{proxy_group}
    '''.format(
            proxy_group=self.proxy_group
        )
