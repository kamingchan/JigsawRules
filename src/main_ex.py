from rules.akamai import Akamai
from rules.antispoofing import *
from rules.apple import *
from rules.chnip import CHNIP
from rules.cloudspeed import CloudSpeed
from rules.final import Final
from rules.home import Home
from rules.lanip import LANIP
from rules.line import Line
from rules.netflix import Netflix
from rules.telegram import Telegram

HOME = '🇨🇳 Home'
DEFAULT_PROXY = 'DEFAULT_PROXY'
UNLIMITED = 'FREE_PROXY'
DIRECT = 'DIRECT'
ASIA = 'ASIA_PROXY'
HK = 'HONGKONG_PROXY'

if __name__ == '__main__':
    rules = [
        Home(HOME),
        CloudSpeed(DIRECT),
        YouTube(UNLIMITED),
        Google(ASIA),
        Twitter(ASIA),
        Facebook(DEFAULT_PROXY),
        Akamai(DEFAULT_PROXY),
        Telegram(ASIA),
        AppleMaps(DIRECT),
        AppleMusic(UNLIMITED),
        iCloud(UNLIMITED),
        Line(ASIA),
        Netflix(HK),
        LANIP(DIRECT),
        CHNIP(DIRECT),
        Final(DEFAULT_PROXY),
    ]
    [print(rule) for rule in rules]
