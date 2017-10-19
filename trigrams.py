"""Trigram.py takes in a text and creates a trigram."""


import random
import sys


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
    """Open source text and create book."""
    new_book = ""
    with open(url_path) as data:
        sherlock = data.read()
    sherlock_list = sherlock.split(' ')
    trigrams(sherlock_list, num)
    for i in range(int(num)):
        new_book += " " + random.choice(list(trigram_list.keys()))
    print(new_book)


trigram_list = {}


def trigrams(sherlock_list, r):
    """Make list then use it to create dictionary."""
    for i in range(r):
        print(trigram_list)
        trigram_list[
            (sherlock_list[i] + ' ' + sherlock_list[i + 1])
            ] = sherlock_list[i + 2]
    return trigram_list


if __name__ == '__main__':
    # pragma: no cover

    url_path, num = sys.argv[1], int(sys.argv[2])
    main(url_path, num)
