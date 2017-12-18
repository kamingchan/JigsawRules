from rules.rules import Rules


class Slack(Rules):
    def __str__(self):
        return '''# Rule for Slack
DOMAIN-SUFFIX,slack.com,{proxy_group}
DOMAIN-SUFFIX,slack-edge.com,{proxy_group}
USER-AGENT,com.tinyspeck.chatlyio/*,{proxy_group}
USER-AGENT,Slack/*,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
