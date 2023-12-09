import hashlib
import typing
import unittest

from data import data, example


Input = str


def parse(input: str) -> Input:
    return input


def part1(input: Input):
    for n in range(1, 1000000):
        if hashlib.md5(f'{input}{n}'.encode("ascii")).hexdigest().startswith("00000"):
            return n
    return 0


def part2(input: Input):
    for n in range(1, 10000000):
        if hashlib.md5(f'{input}{n}'.encode("ascii")).hexdigest().startswith("000000"):
            return n
    return 0


class Tests(unittest.TestCase):
    def test_part1_example_answer(self):
        self.assertEqual(609043, part1(parse(example)))

    def test_part1_answer(self):
        self.assertEqual(282749, part1(parse(data)))

    def test_part2_answer(self):
        self.assertEqual(9962624, part2(parse(data)))


if __name__ == "__main__":
    unittest.main()
