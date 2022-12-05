def read_input(name='input', strip=True):
    with open(f'{name}.txt', 'r') as f:
        data = list(map(lambda x: str(x).strip() if strip else x, f.readlines()))
    return data
