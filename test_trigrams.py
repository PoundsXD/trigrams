"""Test trigrams module."""

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
sherlock_list = sherlock.split(' ')


def test_main():
    """Test main output function."""
    from trigrams import main
    res = main('LICENSE', 5)
    assert res >= 1


def test_tri_0():
    """Test trigram function."""
    from trigrams import trigrams
    assert trigrams(sherlock_list, 0) == 0


def test_tri_1():
    """Test trigram function."""
    from trigrams import trigrams
    assert trigrams(sherlock_list, 10) is not {}
