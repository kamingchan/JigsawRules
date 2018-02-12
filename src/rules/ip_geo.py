from rules.rules import Rules


class IPGeo(Rules):
    def __str__(self):
        return '''# Rule for IP Geo
DOMAIN-SUFFIX,ipip.net,{proxy_group}
DOMAIN-SUFFIX,ip.cn,{proxy_group}
DOMAIN-SUFFIX,ip.sb,{proxy_group}
DOMAIN-SUFFIX,whatismyip.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
