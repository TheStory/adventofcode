from functools import reduce
from math import floor

from year2022 import read_input


class Monkey:
    def __init__(self, index):
        self.index = index
        self.items = []
        self.operation = None
        self.divisible_by = None
        self.target_monkey_if_true = None
        self.target_monkey_if_false = None
        self.inspected_items = 0

    def round(self, divide_worry_level=True):
        throws = []
        for item in self.items:
            self.inspected_items += 1
            old = item
            if divide_worry_level:
                worry_level = floor(eval(self.operation) / 3)
            else:
                worry_level = eval(self.operation)

            if worry_level % self.divisible_by == 0:
                target_monkey = self.target_monkey_if_true
            else:
                target_monkey = self.target_monkey_if_false
            throws.append((target_monkey, worry_level))
        self.items = []
        return throws


def line_startswith(line, pattern):
    return line.strip().startswith(pattern)


def get_line_value(line):
    return line.strip().split(':')[1].strip()


def day_11(data, variant_2=False):
    monkeys = []
    current_monkey = None
    for line in data:
        line = str(line)
        if line_startswith(line, 'Monkey'):
            current_monkey = Monkey(len(monkeys))
            monkeys.append(current_monkey)
        if line_startswith(line, 'Starting items'):
            current_monkey.items = [int(x) for x in get_line_value(line).split(',')]
        if line_startswith(line, 'Operation'):
            current_monkey.operation = get_line_value(line).split(' = ')[-1]
        if line_startswith(line, 'Test'):
            current_monkey.divisible_by = int(get_line_value(line).split(' ')[-1])
        if line_startswith(line, 'If true'):
            current_monkey.target_monkey_if_true = int(get_line_value(line).split(' ')[-1])
        if line_startswith(line, 'If false'):
            current_monkey.target_monkey_if_false = int(get_line_value(line).split(' ')[-1])

    rounds = 10000 if variant_2 else 20
    for r in range(0, rounds):
        print(r, flush=True)
        for m in monkeys:
            if m.items:
                throws = m.round(not variant_2)
                for target, item in throws:
                    monkeys[target].items.append(item)

    monkeys.sort(key=lambda x: x.inspected_items, reverse=True)

    monkey_business = reduce(lambda a, b: a.inspected_items * b.inspected_items, monkeys[0:2])
    print(monkey_business)
    return monkey_business


day_11(read_input(custom_path='data/day_11.txt'), variant_2=True)
