import pytest


def test_cyclic_reference():
    a = {}
    b = {}
    a['b'] = b
    b['a'] = a
    del a
    del b

    with pytest.raises(NameError):
        a['b'] = b
