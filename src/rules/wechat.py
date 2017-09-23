from rules.rules import Rules


class WeChat(Rules):
    def __str__(self):
        return '''# Rule for WeChat
USER-AGENT,MicroMessenger Client,{proxy_group}
USER-AGENT,WeChat/*,{proxy_group}
DOMAIN-SUFFIX,mmbiz.qpic.cn,{proxy_group}
DOMAIN-SUFFIX,weixin.qq.com,{proxy_group}
DOMAIN-SUFFIX,wx.qq.com,{proxy_group}
DOMAIN-SUFFIX,weixinbridge.com,{proxy_group}
DOMAIN-SUFFIX,servicewechat.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
