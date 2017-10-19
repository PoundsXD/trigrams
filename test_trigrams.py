"""."""


# def test_main():
    # """."""


def test_tri_0():
    from trigrams import trigrams
    assert len(trigrams(0)) == 0


def test_tri_20():
    from trigrams import trigrams
    assert len(trigrams(20)) == 19
