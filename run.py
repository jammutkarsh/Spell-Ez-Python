import random as r
import tts
import urllib3
# To disable the error below.
#   InsecureRequestWarning: Unverified HTTPS request is being made to host 'translate.google.com'.
#   Adding certificate verification is strongly advised.
#   See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning,
urllib3.disable_warnings()

with open('wordlist.txt') as f:
    wordlist = f.readlines()

random_word = r.choice(wordlist)

tts.convert(random_word)


