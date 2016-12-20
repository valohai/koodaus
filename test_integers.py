from random import randint
import pytest
from koodaus.integers import decode_int, encode_int


@pytest.mark.parametrize('t', range(8, 65, 8))
def test_integers(t):
    val = randint(1 << t, 1 << (t + 2))
    enc = encode_int(val)
    dec = decode_int(enc)
    assert dec == val


def test_negative_int():
    with pytest.raises(ValueError):
        encode_int(-1)
