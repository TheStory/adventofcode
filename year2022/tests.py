from year2022.day_1 import day_1
from year2022.day_2 import day_2
from year2022.day_3 import day_3
from year2022.day_4 import day_4
from year2022.day_5 import day_5


def test_day_1():
    test_data = [
        '1000',
        '2000',
        '3000',
        '',
        '4000',
        '',
        '5000',
        '6000',
        '',
        '7000',
        '8000',
        '9000',
        '',
        '10000',
    ]
    assert day_1(test_data) == 45000
    assert day_1() == 208567


def test_day_2():
    test_data = [
        'A Y',
        'B X',
        'C Z',
    ]
    assert day_2(test_data) == (15, 12)
    assert day_2() == (11841, 13022)


def test_day_3():
    test_data = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]
    assert day_3(test_data) == (157, 70)
    assert day_3() == (7737, 2697)


def test_day_4():
    test_data = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8',
    ]
    assert day_4(test_data) == (2, 4)
    assert day_4() == (441, 861)


def test_day_5():
    assert list(day_5()) == ['TLNGFGMFN', 'FGLQJCMBD']
