from rules.rules import Rules


class Line(Rules):
    def __str__(self):
        return '''# Rule for Line
DOMAIN-SUFFIX,lin.ee,{proxy_group}
DOMAIN-SUFFIX,line.me,{proxy_group}
DOMAIN-SUFFIX,line.naver.jp,{proxy_group},force-remote-dns // via raw TCP
DOMAIN-SUFFIX,line-apps.com,{proxy_group}
DOMAIN-SUFFIX,line-cdn.net,{proxy_group}
DOMAIN-SUFFIX,line-scdn.net,{proxy_group}
DOMAIN-SUFFIX,nhncorp.jp,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
