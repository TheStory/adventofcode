from functools import reduce

from year2022.utils import read_input

letter_ascii_codes = list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))


def letter_priority(letter):
    return letter_ascii_codes.index(ord(letter)) + 1


input_data = read_input()
# input_data = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
#               'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

priority_sum = 0
for rucksack in input_data:
    compartment_1, compartment_2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    in_both_compartments = list(set(compartment_1) & set(compartment_2))[0]
    priority_sum += letter_priority(in_both_compartments)

print('Priority sum:', priority_sum)

groups = {}
for idx, rucksack in enumerate(input_data):
    rucksack_group = idx // 3
    if rucksack_group not in groups:
        groups[rucksack_group] = []
    groups[rucksack_group].append(rucksack)

badges_priority_sum = 0
for group_idx in groups:
    badge = list(reduce(lambda a, b: a & set(b), list(map(lambda x: set(x), groups[group_idx]))))[0]
    badges_priority_sum += letter_priority(badge)

print('Badges priority:', badges_priority_sum)
