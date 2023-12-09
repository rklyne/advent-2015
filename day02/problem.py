import typing
import unittest

from data import data, example


Triple = typing.Tuple[int, int, int]
Input = list[Triple]


def parse(input: str) -> Input:
    return [
        (int(a), int(b), int(c))
        for (a, b, c) in map(lambda s: s.split("x"), input.split("\n"))
    ]


def paper(t: Triple) -> int:
    (a, b, c) = t
    x = a * b
    y = a * c
    z = b * c
    return 2 * (x + y + z) + min(x, y, z)


def ribbon(t: Triple) -> int:
    (a, b, c) = sorted(t)
    return 2 * (a + b) + (a*b*c)


def part1(input: Input):
    return sum([
        paper(t)
        for t in input
    ])


def part2(input: Input):
    return sum(map(ribbon, input))


class Tests(unittest.TestCase):
    def test_parse(self):
        self.assertEqual((20, 3, 11), parse(data)[0])

    def test_part1_example_answer(self):
        self.assertEqual(58 + 43, part1(parse(example)))

    def test_part1_answer(self):
        self.assertEqual(1606483, part1(parse(data)))

    def test_part2_example_answer(self):
        self.assertEqual(48, part2(parse(example)))

    def test_part2_answer(self):
        self.assertEqual(3842356, part2(parse(data)))


if __name__ == "__main__":
    unittest.main()
