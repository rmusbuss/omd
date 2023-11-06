from one_hot_encoder import fit_transform


def test_ohe1():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_ohe2():
    actual = fit_transform(['Russia', 'USA', 'Russia', 'Great Britain'])
    expected = [
        ('Russia', [0, 0, 1]),
        ('USA', [0, 1, 0]),
        ('Russia', [0, 0, 1]),
        ('Great Britain', [1, 0, 0]),
    ]
    assert actual == expected


def test_ohe3():
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
        assert expected_val in actual


def test_ohe4():
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
        assert not_expected_val not in actual


def test_ohe5():
    try:
        fit_transform()
    except TypeError:
        pass


if __name__ == '__main__':
    pass
