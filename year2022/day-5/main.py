import copy
import re

from year2022 import read_input

gifts_stack = read_input(strip=False)

stack_data_last_line = 8
columns_amount = 9
operations_start_line = 10

current_gift_stack_v1 = {}
current_gift_stack_v2 = {}

for row in gifts_stack[0:stack_data_last_line]:
    for col_idx in range(0, columns_amount):
        if col_idx not in current_gift_stack_v1:
            current_gift_stack_v1[col_idx] = []
        gift_box = row[col_idx * 4:col_idx * 4 + 3].strip()
        if gift_box != '':
            current_gift_stack_v1[col_idx].insert(0, gift_box)
    current_gift_stack_v2 = copy.deepcopy(current_gift_stack_v1)

for operation in gifts_stack[operations_start_line:]:
    move_rgx = r"move ([0-9]*) from ([0-9]*) to ([0-9]*)"
    matches = re.finditer(move_rgx, operation)
    for i, match in enumerate(matches, start=1):
        amount, from_col, to_col = [int(x) for x in match.groups()]
        from_col -= 1
        to_col -= 1
        # part 1 of the task
        for it in range(0, amount):
            from_col_state = current_gift_stack_v1[from_col]
            current_gift_stack_v1[to_col].append(from_col_state[-1])
            current_gift_stack_v1[from_col] = from_col_state[:-1]
        # part 2 of the task
        from_col_state = current_gift_stack_v2[from_col]
        moving_part = from_col_state[-amount:]
        current_gift_stack_v2[to_col] = current_gift_stack_v2[to_col] + moving_part
        current_gift_stack_v2[from_col] = from_col_state[:-amount]

for stack in [current_gift_stack_v1, current_gift_stack_v2]:
    for col_idx in stack:
        if len(stack[col_idx]) > 0:
            print(str(stack[col_idx][-1]).strip('[]'), end='')
        else:
            print(' ', end='')
    print()
