import re

from year2022 import read_input


def day_7(test_data=None, variant_2=False):
    data = test_data or read_input()
    curr_path = ''
    dir_sizes = {}
    for line in data:
        if line.startswith('$ cd'):
            destination = line[5:]
            if destination == '/':
                curr_path = 'root'
            elif destination == '..':
                curr_path = '/'.join(curr_path.split('/')[:-1])
            else:
                curr_path += '/' + destination
        else:
            if curr_path not in dir_sizes:
                dir_sizes[curr_path] = 0
            match = re.match(r'^([0-9]+) .*$', line)
            if match:
                filesize = int(match.groups()[0])
                dir_sizes[curr_path] += filesize
                for idx, path in enumerate(dir_sizes):
                    if path != curr_path and curr_path.startswith(path):
                        dir_sizes[path] += filesize
    if not variant_2:
        result = 0
        for idx, name in enumerate(dir_sizes):
            if dir_sizes[name] <= 100000:
                result += dir_sizes[name]
        return result
    else:
        available_space = 70000000
        required_space = 30000000
        sizes_only = []
        for idx, name in enumerate(dir_sizes):
            if name != 'root':
                sizes_only.append(dir_sizes[name])
        sizes_only.sort()
        for size in sizes_only:
            root_size = available_space - dir_sizes['root'] + size
            if root_size > required_space:
                return size
