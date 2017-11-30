from rules.rules import Rules


class CloudFront(Rules):
    def __str__(self):
        return '''# Rule for Amazon CloudFront
DOMAIN-SUFFIX,cloudfront.net,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
