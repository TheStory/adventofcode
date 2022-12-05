class Elf:
    def __init__(self, index):
        self.name = f'Elf {index}'
        self.calories = 0

    def __repr__(self):
        return f'{self.name}: {self.calories}'
