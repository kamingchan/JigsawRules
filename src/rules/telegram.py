from rules.rules import Rules


class Telegram(Rules):
    def __str__(self):
        return '''# Rule for Telegram
USER-AGENT,*.Telegraph/*,{proxy_group}
USER-AGENT,*.Telegram/*,{proxy_group}
IP-CIDR,109.239.140.0/24,{proxy_group},no-resolve
IP-CIDR,149.154.160.0/22,{proxy_group},no-resolve
IP-CIDR,149.154.164.0/22,{proxy_group},no-resolve
IP-CIDR,149.154.168.0/22,{proxy_group},no-resolve
IP-CIDR,149.154.172.0/22,{proxy_group},no-resolve
IP-CIDR,91.108.4.0/22,{proxy_group},no-resolve
IP-CIDR,91.108.56.0/22,{proxy_group},no-resolve
DOMAIN-SUFFIX,t.me,{proxy_group}
DOMAIN-SUFFIX,telegram.org,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
