from rules.rules import Rules


class System(Rules):
    def __str__(self):
        return '''# bypass system
IP-CIDR,17.0.0.0/8,DIRECT,no-resolve
DOMAIN,api.smoot.apple.com,DIRECT,force-remote-dns
DOMAIN,api.smoot.apple.com.cn,DIRECT,force-remote-dns
DOMAIN,configuration.apple.com,DIRECT,force-remote-dns
DOMAIN,xp.apple.com,DIRECT,force-remote-dns
DOMAIN,smp-device-content.apple.com,DIRECT,force-remote-dns
DOMAIN,guzzoni.apple.com,DIRECT,force-remote-dns
DOMAIN,captive.apple.com,DIRECT,force-remote-dns
DOMAIN-SUFFIX,ess.apple.com,DIRECT,force-remote-dns
DOMAIN-SUFFIX,push.apple.com,DIRECT,force-remote-dns
DOMAIN-SUFFIX,push-apple.com.akadns.net,DIRECT,force-remote-dns
'''
