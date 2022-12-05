from year2022.utils import read_input

# input_data = [
#     '2-4,6-8',
#     '2-3,4-5',
#     '5-7,7-9',
#     '2-8,3-7',
#     '6-6,4-6',
#     '2-6,4-8',
# ]
work_pairs = read_input()


def unpack_elf_from_string(input_row):
    def parse_from_to(elf):
        return [int(x) for x in elf.strip().split('-')]

    elf_1, elf_2 = input_row.split(',')
    from_1, to_1 = parse_from_to(elf_1)
    from_2, to_2 = parse_from_to(elf_2)
    return from_1, to_1, from_2, to_2


complete_overlap = 0
partial_overlap = 0
for pair in work_pairs:
    elf_1_from, elf_1_to, elf_2_from, elf_2_to = unpack_elf_from_string(pair)
    if (elf_1_from >= elf_2_from and elf_1_to <= elf_2_to) or (elf_2_from >= elf_1_from and elf_2_to <= elf_1_to):
        complete_overlap += 1
    if len(list(set(range(elf_1_from, elf_1_to + 1)) & set(range(elf_2_from, elf_2_to + 1)))) > 0:
        partial_overlap += 1

print('Complete:', complete_overlap)
print('Partial:', partial_overlap)
