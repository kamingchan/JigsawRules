from rules.rules import Rules


class AppleMaps(Rules):
    def __str__(self):
        return '''# Rule for Apple Maps
DOMAIN-SUFFIX,ls.apple.com,{proxy_group} // Apple Maps location detective, use local maps
'''.format(
            proxy_group=self.proxy_group
        )


class iCloud(Rules):
    def __str__(self):
        return '''# Rule for iCloud
DOMAIN-SUFFIX,icloud.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )


class AppleMusic(Rules):
    def __str__(self):
        return '''# Rule for Apple Music
DOMAIN-SUFFIX,se2.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,radio.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,radio-activity.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,radio-services.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,aod.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,streamingaudio.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,search.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,api.itunes.apple.com,{proxy_group}
DOMAIN-SUFFIX,audio.itunes.apple.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
