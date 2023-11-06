from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def test_ohe1(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_ohe2(self):
        actual = fit_transform(['Russia', 'USA', 'Russia', 'Great Britain'])
        expected = [
            ('Russia', [0, 0, 1]),
            ('USA', [0, 1, 0]),
            ('Russia', [0, 0, 1]),
            ('Great Britain', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_ohe3(self):
        actual = fit_transform(['Crock', 'Pot', 'Pasta',
                                'Pasta', 'Pomodoro', 'Fresh'])
        expected = [
            ('Crock',
             [0, 0, 0, 0, 1]),
            ('Pot',
             [0, 0, 0, 1, 0]),
            ('Pasta',
             [0, 0, 1, 0, 0]),
            ('Pasta',
             [0, 0, 1, 0, 0]),
            ('Pomodoro',
             [0, 1, 0, 0, 0]),
            ('Fresh',
             [1, 0, 0, 0, 0])
        ]
        for expected_val in expected:
            self.assertIn(expected_val, actual)

    def test_ohe4(self):
        actual = fit_transform(['Python', 'is', 'best', 'programming',
                                'language', 'C++', 'is', 'hardest',
                                'programming', 'language'])
        not_expected = [
            ('Crock',
             [0, 0, 0, 0, 1]),
            ('Pot',
             [0, 0, 0, 1, 0]),
            ('Pasta',
             [0, 0, 1, 0, 0]),
            ('Pasta',
             [0, 0, 1, 0, 0]),
            ('Pomodoro',
             [0, 1, 0, 0, 0]),
            ('Fresh',
             [1, 0, 0, 0, 0])
        ]
        for not_expected_val in not_expected:
            self.assertNotIn(not_expected_val, actual)

    def test_ohe5(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    pass
