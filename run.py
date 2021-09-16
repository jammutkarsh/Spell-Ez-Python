import random as r
import tts  # tts.py
import urllib3

# To disable the error below.
#   InsecureRequestWarning: Unverified HTTPS request is being made to host 'translate.google.com'.
#   Adding certificate verification is strongly advised.
#   See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning,
urllib3.disable_warnings()


def pick_word():
    file = open('wordlist.txt', 'r')
    word_list = file.readlines()
    i = r.randint(0, len(word_list))
    tts.convert(word_list[i])
    return word_list[i]


end_of_game = False

while not end_of_game:
    spell_out = pick_word()
    userInput = input(f"{len(spell_out) - 1} letter word\nEnter Here: ")
    if spell_out.strip('\n') == userInput:
        print("Correct Spelling\n")
    else:
        print("Incorrect Spelling\n")
