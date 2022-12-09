from typing import List

from year2022 import read_input


class Tree:
    forest = None

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def __repr__(self):
        return self.size

    @property
    def scenic_score(self):
        def calc_score(other_sizes):
            score = 0
            for size in other_sizes:
                if size < self.size:
                    score += 1
                if size >= self.size:
                    score += 1
                    break
            return score

        left, right, top, bottom = self.surrounding_sizes

        left.reverse()
        top.reverse()

        left_score = calc_score(left)
        right_score = calc_score(right)
        top_score = calc_score(top)
        bottom_score = calc_score(bottom)

        return left_score * right_score * top_score * bottom_score

    @property
    def is_visible(self):
        if self.x == 0 or self.y == 0 or self.x == self.forest.width - 1 or self.y == self.forest.height - 1:
            return True
        left, right, top, bottom = self.max_sizes_of_surrounding_trees
        return self.size > left or self.size > right or self.size > top or self.size > bottom

    @property
    def surrounding_sizes(self):
        in_row_x = self.forest.get_trees_in_row_x(self.x)
        in_row_y = self.forest.get_trees_in_row_y(self.y)
        x_index_of_tree = in_row_x.index(self)
        y_index_of_tree = in_row_y.index(self)

        left = self.sizes_of_trees_row(in_row_x)[0: x_index_of_tree]
        right = self.sizes_of_trees_row(in_row_x)[x_index_of_tree + 1:]
        top = self.sizes_of_trees_row(in_row_y)[0: y_index_of_tree]
        bottom = self.sizes_of_trees_row(in_row_y)[y_index_of_tree + 1:]

        return left, right, top, bottom

    @property
    def max_sizes_of_surrounding_trees(self):
        left, right, top, bottom = self.surrounding_sizes
        return max(left), max(right), max(top), max(bottom)

    @staticmethod
    def sizes_of_trees_row(row):
        return [x.size for x in row]


class Forest:
    def __init__(self):
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)
        tree.forest = self

    @property
    def width(self):
        return max([x.x for x in self.trees]) + 1

    @property
    def height(self):
        return max([x.y for x in self.trees]) + 1

    def get_trees_in_row_x(self, x) -> List[Tree]:
        return list(filter(lambda t: t.x == x, self.trees))

    def get_trees_in_row_y(self, y) -> List[Tree]:
        return list(filter(lambda t: t.y == y, self.trees))


def day_8(test_data=None, variant_2=False):
    data = test_data or read_input()
    visible_amount = 0
    forest = Forest()

    for x, line in enumerate(data):
        for y, size in enumerate(line):
            forest.add_tree(Tree(x, y, int(size)))

    if not variant_2:
        for tree in forest.trees:
            if tree.is_visible:
                visible_amount += 1
        return visible_amount

    return max([x.scenic_score for x in forest.trees])

