import sys

import pytest


@pytest.mark.skip(reason='deprecated functionality')
def test_mark_skip():
    """Удобен, когда мы разрабатываем"""
    assert 1 == 2


@pytest.mark.skipif(sys.version_info > (3, 0), reason='requires python2')
def test_run_only_for_python_2():
    assert 1 == 2


@pytest.mark.xfail
def test_expecting_fail():
    """Skip недостаточно, этот тест всегда должен быть failed"""
    assert 1 == 2


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_expecting_specific_fail():
    assert 1 / 0
