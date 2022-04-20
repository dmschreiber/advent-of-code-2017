import unittest
import day4
import day5
import day6


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

    def test_day6(self):
        input = "0 2 7 0"
        self.assertEqual(day6.redistribute(input),"2 4 1 2")
        self.assertEqual(day6.redistribute("2 4 1 2"),"3 1 2 3")
        self.assertEqual(day6.redistribute("3 1 2 3"),"0 2 3 4")
        self.assertEqual(day6.redistribute("0 2 3 4"),"1 3 4 1")
        self.assertEqual(day6.redistribute("1 3 4 1"),"2 4 1 2")
        self.assertEqual(day6.part1(input),5)

if __name__ == '__main__':
    unittest.main()
