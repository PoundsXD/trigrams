"""Trigram.py takes in a text and creates a trigram."""


import random
import sys

trigram_list = {}


def main(url_path, num):
    """Open source text and create book."""
    new_book = ""
    with open(url_path) as data:
        sherlock = data.read()
    sherlock_list = sherlock.split(' ')
    print(sherlock_list)
    trigrams(sherlock_list, num)
    for i in range(int(num)):
        new_book += " " + random.choice(list(trigram_list.keys()))
    return new_book


def trigrams(sherlock_list, r):
    """Make list then use it to create dictionary."""
    if r == 0:
        return 0
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
