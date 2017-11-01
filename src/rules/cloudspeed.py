from rules.rules import Rules


class CloudSpeed(Rules):
    def __str__(self):
        return '''# Rule for CloudSpeed
USER-AGENT,CloudSpeed/*,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
