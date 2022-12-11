from year2022 import read_input


class Knot:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.visited_positions = {'1,1'}

    def __repr__(self):
        return f'[{self.x},{self.y}]'

    def move(self, direction):
        if direction == 'L':
            self.x -= 1
        if direction == 'R':
            self.x += 1
        if direction == 'D':
            self.y -= 1
        if direction == 'U':
            self.y += 1

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def mark_as_visited(self):
        self.visited_positions.add(f'{self.x},{self.y}')

    @property
    def positions_visited(self):
        return len(self.visited_positions)


class Rope:
    def __init__(self, knots_amount):
        self.knots = [Knot() for x in range(0, knots_amount)]

    @property
    def head(self):
        return self.knots[0]

    @property
    def tail(self):
        return self.knots[-1]

    def move_head(self, direction, steps):
        for step in range(0, steps):
            self.head.move(direction)
            for idx in range(1, len(self.knots)):
                knot = self.knots[idx]
                prev_knot = self.knots[idx - 1]
                if not self.are_knots_touching(prev_knot, knot):
                    if prev_knot.x == knot.x or prev_knot.y == knot.y:
                        if prev_knot.x == knot.x:
                            if prev_knot.y > knot.y:
                                knot.move('U')
                            if prev_knot.y < knot.y:
                                knot.move('D')
                        if prev_knot.y == knot.y:
                            if prev_knot.x > knot.x:
                                knot.move('R')
                            if prev_knot.x < knot.x:
                                knot.move('L')
                    else:
                        if prev_knot.x > knot.x:
                            knot.move('R')
                        if prev_knot.x < knot.x:
                            knot.move('L')
                        if prev_knot.y > knot.y:
                            knot.move('U')
                        if prev_knot.y < knot.y:
                            knot.move('D')
                knot.mark_as_visited()

    @staticmethod
    def are_knots_touching(knot_1, knot_2):
        x_coordinates = [knot_1.x, knot_2.x]
        y_coordinates = [knot_1.y, knot_2.y]
        return max(x_coordinates) - min(x_coordinates) <= 1 and max(y_coordinates) - min(y_coordinates) <= 1


def day_9(test_data=None):
    data = test_data or read_input()

    rope = Rope(2)
    multi_knot_rope = Rope(10)
    for move in data:
        direction, steps = str(move).split(' ')
        rope.move_head(direction, int(steps))
        multi_knot_rope.move_head(direction, int(steps))

    return rope, multi_knot_rope
