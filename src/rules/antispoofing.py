from rules.rules import Rules


class AntiSpoofing(Rules):
    def __str__(self):
        return '''# Rule for DNS poisoning with raw TCP connection
DOMAIN-SUFFIX,facebook.com,{proxy_group},force-remote-dns // Facebook
DOMAIN-SUFFIX,fbcdn.net,{proxy_group},force-remote-dns // Facebook
DOMAIN-SUFFIX,fbsbx.com,{proxy_group},force-remote-dns // Facebook

DOMAIN-KEYWORD,google,{proxy_group},force-remote-dns // Google
DOMAIN-KEYWORD,youtube,{proxy_group},force-remote-dns // Google
DOMAIN-KEYWORD,gmail,{proxy_group},force-remote-dns // Google
DOMAIN-SUFFIX,ggpht.com,{proxy_group},force-remote-dns // Google
DOMAIN-SUFFIX,gstatic.com,{proxy_group},force-remote-dns // Google
DOMAIN-SUFFIX,g.co,{proxy_group},force-remote-dns // Google
DOMAIN-SUFFIX,goo.gl,{proxy_group},force-remote-dns // Google

DOMAIN-SUFFIX,youtu.be,{proxy_group},force-remote-dns // YouTube
DOMAIN-SUFFIX,ytimg.com,{proxy_group},force-remote-dns // YouTube

DOMAIN-KEYWORD,twitter,{proxy_group},force-remote-dns // Twitter
DOMAIN-SUFFIX,t.co,{proxy_group},force-remote-dns // Twitter
DOMAIN-SUFFIX,twimg.com,{proxy_group},force-remote-dns // Twitter

'''.format(
            proxy_group=self.proxy_group
        )
