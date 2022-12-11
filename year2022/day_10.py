from year2022 import read_input


def day_10(test_data=None):
    commands = test_data or read_input()

    result = 0
    reg_x = 1
    curr_cycle = 1
    executing_command = None
    commands_iterator = iter(commands)
    current_col = 1

    executing = True
    while executing:
        if current_col - 1 in [reg_x - 1, reg_x, reg_x + 1]:
            print('#', end='')
        else:
            print('.', end='')

        if not executing_command:
            executing_command = next(commands_iterator, None)
            if not executing_command:
                executing = False
            else:
                if executing_command == 'noop':
                    executing_command = None
        else:
            reg_x += int(executing_command.split(' ')[1])
            executing_command = None

        curr_cycle += 1
        if curr_cycle in [20, 60, 100, 140, 180, 220]:
            result += reg_x * curr_cycle

        if current_col == 40:
            current_col = 0
            print()

        current_col += 1

    return result
