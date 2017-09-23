from rules.rules import Rules


class Spotify(Rules):
    def __str__(self):
        return '''# Rule for Spotify
USER-AGENT,Spotify/*,{proxy_group}
DOMAIN-SUFFIX,spotify.com,{proxy_group}
DOMAIN-SUFFIX,adjust.com,{proxy_group}
DOMAIN-SUFFIX,scdn.co,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
