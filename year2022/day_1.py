from year2022 import read_input


class Elf:
    def __init__(self, index):
        self.name = f'Elf {index}'
        self.calories = 0

    def __repr__(self):
        return f'{self.name}: {self.calories}'


def day_1(test_data=None):
    data = test_data or read_input()
    elves = [Elf(0)]
    current_elf = 0
    for calories_entry in data:
        if calories_entry != '':
            elves[current_elf].calories += int(calories_entry)
        else:
            current_elf += 1
            elves.append(Elf(current_elf))

    elves.sort(key=lambda e: e.calories)
    elves.reverse()

    return sum(e.calories for e in elves[:3])
