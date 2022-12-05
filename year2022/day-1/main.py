from year2022.models import Elf
from year2022.utils import read_input

elves = [Elf(0)]

current_elf = 0
for line in read_input('input'):
    if line != '':
        elves[current_elf].calories += int(line)
    else:
        current_elf += 1
        elves.append(Elf(current_elf))

elves.sort(key=lambda e: e.calories)
elves.reverse()

print(sum(e.calories for e in elves[:3]))
