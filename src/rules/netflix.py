from rules.rules import Rules


class Netflix(Rules):
    def __str__(self):
        return '''# Rule for Netflix
DOMAIN-SUFFIX,netflix.com,{proxy_group}
DOMAIN-SUFFIX,netflix.net,{proxy_group}
DOMAIN-SUFFIX,nflxext.com,{proxy_group}
DOMAIN-SUFFIX,nflximg.com,{proxy_group}
DOMAIN-SUFFIX,nflximg.net,{proxy_group}
DOMAIN-SUFFIX,nflxvideo.net,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
