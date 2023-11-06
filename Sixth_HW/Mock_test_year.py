import unittest
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    def test_get_cases(self):
        p1 = patch('what_is_year_now.urllib.request.urlopen', MagicMock())
        m = MagicMock(side_effect=[
            {'test_key': 'test_val', 'currentDateTime': '2023-11-01'}])
        p2 = patch('what_is_year_now.json.load', m)
        with p1 as mocked_urlopen, \
                p2 as mocked_jsonload:
            assert what_is_year_now() == 2023

    def test_get_cases_2(self):
        p1 = patch('what_is_year_now.urllib.request.urlopen', MagicMock())
        m = MagicMock(side_effect=[
            {'test_key': 'test_val', 'currentDateTime': '01.11.2023'}])
        p2 = patch('what_is_year_now.json.load', m)
        with p1 as mocked_urlopen, \
                p2 as mocked_jsonload:
            assert what_is_year_now() == 2023

    def test_get_cases_3(self):
        p1 = patch('what_is_year_now.urllib.request.urlopen', MagicMock())
        m = MagicMock(side_effect=[
            {'test_key': 'test_val', 'currentDateTime': '2023/11/01'}])
        p2 = patch('what_is_year_now.json.load', m)
        with p1 as mocked_urlopen, \
                p2 as mocked_jsonload:
            with self.assertRaises(Exception):
                what_is_year_now()

if __name__ == '__main__':
    pass
