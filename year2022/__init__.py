import inspect
from os import path


def read_input(strip=True):
    current_call_frm = inspect.currentframe()
    parent_call_frm = inspect.getouterframes(current_call_frm)
    calling_function_name = parent_call_frm[1].function
    input_file = f'{path.dirname(path.abspath(__file__))}/data/{calling_function_name}.txt'
    with open(input_file, 'r') as f:
        data = list(map(lambda x: str(x).strip() if strip else x, f.readlines()))
    return data
