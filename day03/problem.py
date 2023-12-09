import typing
import unittest

from data import data, example


Input = str


parse = lambda x: x


def part1(input: Input):
    return len(follow_path(input))


def follow_path(input: str) -> int:
    here = (0, 0)
    locations = set([here])
    move = {
        ">": lambda l: (l[0]+1, l[1]),
        "<": lambda l: (l[0]-1, l[1]),
        "^": lambda l: (l[0], l[1]+1),
        "v": lambda l: (l[0], l[1]-1),
    }
    for c in input:
        here = move[c](here)
        locations.add(here)
    return locations


def part2(input: Input):
    path1 = []
    path2 = []
    while input:
        path1.append(input[0])
        path2.append(input[1])
        input = input[2:]
    return len(follow_path(path1).union(follow_path(path2)))


class Tests(unittest.TestCase):
    def test_part1_example_answer(self):
        self.assertEqual(2, part1(">"))
        self.assertEqual(4, part1("^>v<"))
        self.assertEqual(2, part1("^v^v^v^v^v"))

    def test_part1_answer(self):
        self.assertEqual(2565, part1(parse(data)))

    def test_part2_example_answer(self):
        self.assertEqual(3, part2("^v"))
        self.assertEqual(3, part2("^>v<"))
        self.assertEqual(11, part2("^v^v^v^v^v"))

    def test_part2_answer(self):
        self.assertEqual(2639, part2(parse(data)))


if __name__ == "__main__":
    unittest.main()
