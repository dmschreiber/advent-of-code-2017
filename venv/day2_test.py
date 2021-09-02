import unittest
import day2

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(day2.part1(["5 1 9 5", "7 5 3", "2 4 6 8"]), "18")
        self.assertEqual(day2.part2(["5 9 2 8", "9 4 7 3", "3 8 6 5"]), "9")

if __name__ == '__main__':
    unittest.main()
