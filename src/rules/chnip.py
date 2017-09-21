from rules.rules import Rules


class CHNIP(Rules):
    def __str__(self):
        return '''# For China IP
GEOIP,CN,{proxy_group}
'''.format(
            proxy_group=self.proxy_group
        )
