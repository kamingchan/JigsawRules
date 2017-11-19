from rules.rules import Rules


class Proxy(Rules):
    def __str__(self):
        return '''# Rule for Common Proxy
PROCESS-NAME,v2ray,{proxy_group}
PROCESS-NAME,ss-*,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
