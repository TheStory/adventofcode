from year2022 import read_input


def day_6(test_data=None, part_2=False):
    buff = ''
    buff_size = 14 if part_2 else 4
    data = test_data or read_input()[0]
    for idx, c in enumerate(data):
        if len(buff) == buff_size:
            buff = buff[1:] + c
            if len(set(buff)) == buff_size:
                return idx + 1
        else:
            buff += c
    return 0
