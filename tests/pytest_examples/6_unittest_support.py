import pytest
import unittest


@pytest.fixture(scope='class')
def db_class(request):
    class DummyDB:
        def __init__(self):
            self.opened = True

        def close(self):
            self.opened = False

        def open(self):
            self.opened = True

    request.cls.db = DummyDB()


@pytest.mark.usefixtures('db_class')
class TestDB(unittest.TestCase):
    def test_closing(self):
        self.db.close()
        assert self.db.opened is False

    def test_opening_for_unittest_assert(self):
        self.db.open()
        self.assertTrue(self.db.opened)
