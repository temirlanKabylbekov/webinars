"""https://docs.pytest.org/en/stable/reference.html?highlight=pytest_sessionfinish#hooks"""
import gc
import warnings


def pytest_addoption(parser):
    parser.addoption('--gc-collect', action='store_true', default=False, help='Запуск GC после каждого теста')


def pytest_runtest_teardown(item, nextitem):
    if item.config.getoption('--gc-collect'):
        non_reachable_objects_count = gc.collect()
        if non_reachable_objects_count > 0:
            warnings.warn(f'нужен сборщик циклических ссылок в тесте: {item.name}')
    return nextitem
