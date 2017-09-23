from rules.rules import Rules


class Instagram(Rules):
    def __str__(self):
        return '''# Rule for Instagram
USER-AGENT,Instagram*,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
