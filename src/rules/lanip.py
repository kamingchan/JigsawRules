from rules.rules import Rules


class LANIP(Rules):
    def __str__(self):
        return '''# For Lan IP
DOMAIN-SUFFIX,local,{proxy_group}
IP-CIDR,192.168.0.0/16,{proxy_group}
IP-CIDR,10.0.0.0/8,{proxy_group}
IP-CIDR,172.16.0.0/12,{proxy_group}
IP-CIDR,127.0.0.1/8,{proxy_group}
IP-CIDR,100.64.0.0/10,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
