import hashlib
import time

import pytest

@pytest.mark.timeit(n=100000, r=5, mode='fast')
def test_simple():
    s = ""
    for i in range(100):
        s = s + "a"


@pytest.mark.timeit(n=1000000, r=15, mode='fast')
def test_hash():
    hashlib.sha256(b"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
