import inspect
from os import path


def read_input(strip=True, custom_path=None):
    input_file = f'{path.dirname(path.abspath(__file__))}/'
    if not custom_path:
        current_call_frm = inspect.currentframe()
        parent_call_frm = inspect.getouterframes(current_call_frm)
        calling_function_name = parent_call_frm[1].function
        input_file += f'data/{calling_function_name}.txt'
    else:
        input_file += custom_path
    with open(input_file, 'r') as f:
        data = list(map(lambda x: str(x).strip() if strip else x, f.readlines()))
    return data
