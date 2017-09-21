from rules.rules import Rules


class Home(Rules):
    def __str__(self):
        return '''# Rule for back home
DOMAIN-SUFFIX,home,{proxy_group},force-remote-dns // {comment}
'''.format(
            proxy_group=self.proxy_group,
            comment='resolve *.home via ss'
        )
