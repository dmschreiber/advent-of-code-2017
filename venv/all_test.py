import unittest

class MyTestCase(unittest.TestCase):
    def test_day4(self):
        self.assertEqual(day4.part2_validate("iiii oiii ooii oooi oooo"), True)
        self.assertEqual(day4.part2_validate("oiii ioii iioi iiio"), False)
        self.assertEqual(day4.part2_validate("abcde fghij"), True)
        self.assertEqual(day4.part2_validate("abcde xyz ecdab"), False)