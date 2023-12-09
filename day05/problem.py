import typing
import unittest

from data import data, example


Input = str


def parse(input: str) -> Input:
    return input


def vowel_count(s):
    return sum([s.count(l) for l in "aeiou"])


def has_double(s):
    return any([x == y for (x,y) in zip(s, s[1:])])


def has_double_with_repetition(s):
    return any([x == y for (x,y) in zip(s, s[2:])])


def has_double_no_overlap(s):
    for i in range(len(s)):
        if s[i+2:].find(s[i:i+2]) != -1:
            return True
    return False


def contains_any(s, items):
    for i in items:
        if i in s:
            return True
    return False


def is_nice(s):
    forbidden = ["ab", "cd", "pq", "xy"]
    return vowel_count(s) >= 3 and has_double(s) and not contains_any(s, forbidden)


def part1(input: Input):
    return len(list(filter(is_nice, input.split("\n"))))


def is_very_nice(s):
    forbidden = ["ab", "cd", "pq", "xy"]
    return has_double_no_overlap(s) and has_double_with_repetition(s)


def part2(input: Input):
    return len(list(filter(is_very_nice, input.split("\n"))))


class Tests(unittest.TestCase):
    def test_nice(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))
        self.assertFalse(is_nice("jchzalrnumimnmhp"))
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))
        self.assertTrue(is_nice("aaa"))

    def test_part1_example_answer(self):
        self.assertEqual(2, part1(parse(example)))

    def test_part1_answer(self):
        self.assertEqual(258, part1(parse(data)))

    def test_part2_answer(self):
        self.assertEqual(53, part2(parse(data)))


if __name__ == "__main__":
    unittest.main()
