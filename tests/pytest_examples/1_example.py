import pytest


def test_simple_assert():
    assert [1, 2, 3] == [1, 2222, 3]



class Tests:
    def test_simple_assert(self):
        assert '.'.join(['1', '2', '3']) in '1.2.3.4'

    def test_expected_exception(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
