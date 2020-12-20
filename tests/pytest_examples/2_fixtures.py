"""
 - fixture dependency
 - fixture calculation
 - fixture factories
 - yield fixtures: setup-teardown (files, transactions, connections)

scopes:
    function (default)
    class
    module
    package
    session

"""
import pytest

import random

SEED_VALUE = 100500


# @pytest.fixture
# def any_integer_value():
#     return 1
#
#
# def test_it_is_instance_of_integer(any_integer_value):
#     assert isinstance(any_integer_value, int)

#
@pytest.fixture
def rnd_gen():
    return random.Random(SEED_VALUE)


@pytest.fixture
def rnd(rnd_gen):
    return rnd_gen.random()
#
#
# def test_fixture_dependency(rnd):
#     assert isinstance(rnd, float)


@pytest.fixture
def rnd1(rnd):
    return rnd


@pytest.fixture
def rnd2(rnd):
    return rnd


def test_fixture_calculation(rnd1, rnd2):
    assert rnd1 != rnd2


@pytest.fixture
def rnd_factory(rnd_gen):
    def factory():
        return rnd_gen.random()
    return factory


def test_fixture_factory(rnd_factory):
    assert rnd_factory() != rnd_factory()


@pytest.yield_fixture
def opened_file():
    f = None

    def opener(filename):
        nonlocal f
        f = open(filename)
        return f

    yield opener

    if f is not None:
        f.close()


def test_resource_cleanup(opened_file):
    assert 'import pytest' in opened_file('2_fixtures.py').read()


class DB:
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        self.intransaction.append(name)

    def rollback(self):
        self.intransaction.pop()


@pytest.fixture(scope='module')
def db():
    return DB()


class TestUsingAutoUse:
    @pytest.fixture(autouse=True)
    def transact_autouse(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method(self, db):
        assert db.intransaction == ['test_method']


@pytest.fixture
def transact_autouse(request, db):
    db.begin(request.function.__name__)
    yield
    db.rollback()


def test_without_using_autouse(transact_autouse, db):
    assert db.intransaction == ['test_without_using_autouse']
