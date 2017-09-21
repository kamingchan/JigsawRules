from rules.rules import Rules


class Akamai(Rules):
    def __str__(self):
        return '''# Rule for Akamai CDN
DOMAIN-KEYWORD,akamai,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
