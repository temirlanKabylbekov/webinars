import pytest
import random

SEED_VALUE = 100500


@pytest.fixture
def rnd_gen():
    return random.Random(SEED_VALUE)


@pytest.fixture
def rnd(rnd_gen):
    return rnd_gen.random()
