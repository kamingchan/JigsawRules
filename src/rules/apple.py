from rules.rules import Rules


class AppleMaps(Rules):
    def __str__(self):
        return '''# Rule for Apple Maps
USER-AGENT,*locationd*,{proxy_group}
USER-AGENT,*geod*,{proxy_group}
DOMAIN-SUFFIX,ls.apple.com,{proxy_group} // Apple Maps location detective, use local maps
'''.format(
            proxy_group=self.proxy_group
        )


class iCloud(Rules):
    def __str__(self):
        return '''# Rule for iCloud
USER-AGENT,*CloudKit*,{proxy_group}
USER-AGENT,*cloudd*,{proxy_group}
DOMAIN-SUFFIX,icloud.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )


class AppleMusic(Rules):
    def __str__(self):
        return '''# Rule for Apple Music
USER-AGENT,*Music*,{proxy_group}
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


class Podcast(Rules):
    def __str__(self):
        return '''# Rule for Podcast App
USER-AGENT,*Podcasts*,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
