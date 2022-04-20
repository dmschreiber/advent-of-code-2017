import unittest
import day4
import day5

class MyTestCase(unittest.TestCase):
    def test_day4(self):
        self.assertEqual(day4.part2_validate("iiii oiii ooii oooi oooo"), True)
        self.assertEqual(day4.part2_validate("oiii ioii iioi iiio"), False)
        self.assertEqual(day4.part2_validate("abcde fghij"), True)
        self.assertEqual(day4.part2_validate("abcde xyz ecdab"), False)

    def test_day5(self):
        input = "./data/day5_test.txt"
        self.assertEqual(day5.part1(input),5)
        self.assertEqual(day5.part2(input),10)

if __name__ == '__main__':
    unittest.main()
