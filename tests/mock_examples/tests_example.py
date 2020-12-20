"""
Для чего нужны моки:
 - создание независимости от внешнего мира, путем подмены реальных объектов
 - считать сколько раз был вызван объект (метод, функция) и как (аргументы)

"""
from requests.exceptions import Timeout

import unittest
from unittest import mock

from example import get_full_user_info


class TestFullGithubUserInfo(unittest.TestCase):
    @mock.patch('example.get_github_user_info', return_value={'name': 'paul', 'followers': 11, 'following': 10})
    def test_success(self, *args):
        self.assertEqual(get_full_user_info('paul'), 'paul | followers: 11 | following: 10')

    @mock.patch('example.requests.get', side_effect=Timeout)
    def test_when_github_is_not_reachable(self, *args):
        self.assertIsNone(get_full_user_info('paul'))

    @mock.patch('example.requests.get')
    def test_external_calls_count(self, mock_request_get):
        for _ in range(3):
            get_full_user_info('paul')

        self.assertEqual(mock_request_get.call_count, 3)
        self.assertEqual(mock_request_get.call_args[0][0], 'https://api.github.com/users/paul')


if __name__ == '__main__':
    unittest.main()
