"""Trigram.py takes in a text and creates a trigram."""


from urllib.request import urlopen
import random



sherlock = 'One night it was on the twentieth of March 1888 I was returning\
    which must always be associated in my mind with my wooing and with the\
    dark incidents of the Study in Scarlet I was seized with a keen desire to\
    see Holmes again and to know how he was employing his extraordinary powers\
    His rooms were brilliantly lit and even as I looked up I saw his tall\
    spare figure pass twice in a dark silhouette against the blind He was\
    pacing the room swiftly eagerly with his head sunk upon his chest and his\
    hands clasped behind him To me who knew his every mood and habit his\
    attitude and manner told their own story He was at work again He had risen\
    out of his drug created dreams and was hot upon the scent of some new\
    problem I rang the bell and was shown up to the chamber which had formerly\
    been in part my own'


def main(url_path, num):
    """."""
    # book_test = ""
    new_book = ""
    with open(url_path) as data:
        sherlock = data.read()
    sherlock_list = sherlock.split(' ')
    # print('book_test' + book_test.decode('utf-8'))
    trigrams(sherlock_list, num)
    for i in range(int(num)):
        new_book += " " + random.choice(list(trigram_list.keys()))
    print(new_book)


trigram_list = {}


def trigrams(sherlock_list, r):
    """."""
    for i in range(r):
        print(trigram_list)
        trigram_list[
            (sherlock_list[i] + ' ' + sherlock_list[i + 1])
            ] = sherlock_list[i + 2]
    # for i in trigram_list:
    #     print(trigram_list[i])
    return trigram_list
