import hashlib
import random
import time

import pytest

@pytest.mark.timeit(n=1000, r=5, mode='fast')
def test_simple():
    s = ""
    for i in range(1000):
        s = s + "a"


@pytest.mark.timeit(n=100000, r=15, mode='fast')
def test_hash():
    hashlib.sha256(b"abcdefghijklmnopqrstuvwxyz")


@pytest.mark.timeit(n=1000, r=3)
def test_hash_safe():
    hashlib.sha256(b"abcdefghijklmnopqrstuvwxyz0")
