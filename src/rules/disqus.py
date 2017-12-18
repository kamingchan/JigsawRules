from rules.rules import Rules


class Disqus(Rules):
    def __str__(self):
        return '''# Rule for Disqus
DOMAIN-SUFFIX,disqus.com,{proxy_group}
DOMAIN-SUFFIX,disquscdn.com,{proxy_group}
DOMAIN-SUFFIX,disq.us,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
