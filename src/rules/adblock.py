import requests

from rules.rules import Rules


class ADBlock(Rules):
    def __init__(self, proxy_group):
        super().__init__(proxy_group)
        hosts_url = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts'
        hosts_list = requests.get(hosts_url).text.split('\n')
        hosts_list = map(lambda x: x.strip(), hosts_list)
        hosts_list = filter(lambda x: not x.startswith('#') and x is not '', hosts_list)
        self.ad_domains = list()
        for host in hosts_list:
            fake_ip, domain = host.split(' ')
            self.ad_domains.append(domain)

    def __str__(self):
        config = map(lambda x: 'DOMAIN-SUFFIX,%s,{proxy_group}' % x, self.ad_domains)
        config = '''# Rule for ADBlock
{config}
'''.format(config='\n'.join(config))
        return config.format(
            proxy_group=self.proxy_group
        )
