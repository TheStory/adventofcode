from year2022 import read_input
from year2022.day_1 import day_1
from year2022.day_10 import day_10
from year2022.day_11 import day_11
from year2022.day_2 import day_2
from year2022.day_3 import day_3
from year2022.day_4 import day_4
from year2022.day_5 import day_5
from year2022.day_6 import day_6
from year2022.day_7 import day_7
from year2022.day_8 import day_8
from year2022.day_9 import day_9, Rope


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


class TestDay6:
    test_data = [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26),
    ]

    def test_part_1(self):
        for test_input, expected_1, expected_2 in self.test_data:
            assert day_6(test_input) == expected_1
        assert day_6() == 1855

    def test_part_2(self):
        for test_input, expected_1, expected_2 in self.test_data:
            assert day_6(test_input, part_2=True) == expected_2
        assert day_6(part_2=True) == 3256


class TestDay7:
    @property
    def test_data(self):
        return read_input(custom_path='data/day_7_test.txt')

    def test_part_1(self):
        assert day_7(self.test_data) == 95437
        assert day_7() == 1845346

    def test_part_2(self):
        assert day_7(self.test_data, variant_2=True) == 24933642
        assert day_7(variant_2=True) == 3636703


class TestDay8:
    test_data = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]

    def test_part_1(self):
        assert day_8(self.test_data) == 21
        assert day_8() == 1681

    def test_part_2(self):
        assert day_8(self.test_data, variant_2=True) == 8
        assert day_8(variant_2=True) == 201684


class TestDay9:
    @property
    def test_data(self):
        return read_input(custom_path='data/day_9_test.txt')

    def test_touch_detection(self):
        rope = Rope(2)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(2, 1)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(3, 1)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(2, 1)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(4, 1)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(3, 1)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 1)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(4, 1)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 2)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 2)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 3)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(5, 2)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 4)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(5, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 5)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(5, 4)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(4, 5)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(3, 5)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(4, 5)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(2, 5)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(3, 5)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(2, 4)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(3, 4)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(4, 4)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 4)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(4, 4)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(6, 4)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(5, 4)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(6, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(5, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(4, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(3, 3)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(4, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(2, 3)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(3, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(1, 3)
        assert not rope.are_knots_touching(rope.head, rope.tail)
        rope.tail.set_position(2, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(2, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)
        rope.head.set_position(3, 3)
        assert rope.are_knots_touching(rope.head, rope.tail)

    def test_move_head(self):
        rope = Rope(2)
        rope.move_head('R', 1)
        assert rope.head.x == 2
        assert rope.head.y == 1
        assert rope.tail.x == 1
        assert rope.tail.y == 1
        rope.move_head('R', 1)
        assert rope.head.x == 3
        assert rope.head.y == 1
        assert rope.tail.x == 2
        assert rope.tail.y == 1
        rope.move_head('R', 1)
        assert rope.head.x == 4
        assert rope.head.y == 1
        assert rope.tail.x == 3
        assert rope.tail.y == 1
        rope.move_head('U', 1)
        assert rope.head.x == 4
        assert rope.head.y == 2
        assert rope.tail.x == 3
        assert rope.tail.y == 1
        rope.move_head('U', 1)
        assert rope.head.x == 4
        assert rope.head.y == 3
        assert rope.tail.x == 4
        assert rope.tail.y == 2
        rope.move_head('R', 1)
        assert rope.head.x == 5
        assert rope.head.y == 3
        assert rope.tail.x == 4
        assert rope.tail.y == 2
        rope.move_head('R', 1)
        assert rope.head.x == 6
        assert rope.head.y == 3
        assert rope.tail.x == 5
        assert rope.tail.y == 3
        rope.move_head('D', 1)
        assert rope.head.x == 6
        assert rope.head.y == 2
        assert rope.tail.x == 5
        assert rope.tail.y == 3
        rope.move_head('D', 1)
        assert rope.head.x == 6
        assert rope.head.y == 1
        assert rope.tail.x == 6
        assert rope.tail.y == 2
        rope.move_head('L', 1)
        assert rope.head.x == 5
        assert rope.head.y == 1
        assert rope.tail.x == 6
        assert rope.tail.y == 2
        rope.move_head('L', 1)
        assert rope.head.x == 4
        assert rope.head.y == 1
        assert rope.tail.x == 5
        assert rope.tail.y == 1

    def test_part_1(self):
        rope, _ = day_9(self.test_data)
        assert rope.tail.positions_visited == 13
        rope, _ = day_9()
        assert rope.tail.positions_visited == 5960

    def test_part_2(self):
        _, rope = day_9(self.test_data)
        assert rope.tail.positions_visited == 1
        _, rope = day_9(read_input(custom_path='data/day_9_test_2.txt'))
        assert rope.tail.positions_visited == 36
        _, rope = day_9()
        assert rope.tail.positions_visited == 2327


class TestDay10:
    def test_all_parts(self):
        assert day_10(read_input(custom_path='data/day_10_test.txt')) == 13140
        print()
        assert day_10() == 13720


class TestDay11:
    def test_part_1(self):
        # assert day_11(read_input(custom_path='data/day_11_test.txt')) == 10605
        # assert day_11(read_input(custom_path='data/day_11.txt')) == 90882
        assert day_11(read_input(custom_path='data/day_11_test.txt'), variant_2=True) == 2713310158
