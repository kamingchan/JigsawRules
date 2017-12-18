from rules.rules import Rules


class Typlog(Rules):
    def __str__(self):
        return '''# Rule for Typlog
DOMAIN-SUFFIX,typlog.com,{proxy_group}
DOMAIN-SUFFIX,typcdn.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
