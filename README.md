# JigsawRules

A easy way to generate your own Surge rules.

## Usage

1. Copy `src/main_ex.py` to `src/main.py`.
2. Edit the proxy group name in `src/main.py` and import rules.
3. `python3 src/main.py > rules.txt`
4. Replace the rules under `[Rule]` in your Surge configuration with rules.txt.

## Pull Request

A rule must inherit from `Rules` and implement `__str__` method. Comment at the first line of rules string are recommended.

```python
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
```
