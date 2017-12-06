from rules.rules import Rules


# Rule for DNS poisoning with raw TCP connection

class Facebook(Rules):
    def __str__(self):
        return '''# Rule for Facebook
DOMAIN-SUFFIX,facebook.com,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,fbcdn.net,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,fbsbx.com,{proxy_group},force-remote-dns
'''.format(
            proxy_group=self.proxy_group
        )


class Google(Rules):
    def __str__(self):
        return '''# Rule for google.com / Gmail
DOMAIN-KEYWORD,google,{proxy_group},force-remote-dns
DOMAIN-KEYWORD,youtube,{proxy_group},force-remote-dns
DOMAIN-KEYWORD,gmail,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,ggpht.com,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,gstatic.com,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,g.co,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,goo.gl,{proxy_group},force-remote-dns
'''.format(
            proxy_group=self.proxy_group
        )


class YouTube(Rules):
    def __str__(self):
        return '''# Rule for YouTube
USER-AGENT,YouTube/*,{proxy_group}
USER-AGENT,com.google.ios.youtube/*,{proxy_group}
DOMAIN-SUFFIX,googlevideo.com,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,youtu.be,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,ytimg.com,{proxy_group},force-remote-dns
'''.format(
            proxy_group=self.proxy_group
        )


class Twitter(Rules):
    def __str__(self):
        return '''# Rule for Twitter
USER-AGENT,Twitter/*,{proxy_group}
USER-AGENT,Twitter-Mac/*,{proxy_group}
USER-AGENT,Tweetbot/*,{proxy_group}
DOMAIN-KEYWORD,twitter,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,t.co,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,twimg.com,{proxy_group},force-remote-dns
DOMAIN-SUFFIX,tapbots.com,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )


class WhatsApp(Rules):
    def __str__(self):
        return '''# Rule for WhatsApp
USER-AGENT,WhatsApp/*,{proxy_group}
DOMAIN-SUFFIX,whatsapp.net,{proxy_group},force-remote-dns
'''.format(
            proxy_group=self.proxy_group
        )
