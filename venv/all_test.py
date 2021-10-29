import unittest
import day3

class MyTestCase(unittest.TestCase):
    def test_day3(self):
        self.assertEqual(day3.part1(1), 0)
        self.assertEqual(day3.part1(12), 3)
        self.assertEqual(day3.part1(20), 3)
        self.assertEqual(day3.part1(16), 3)
        self.assertEqual(day3.part1(23), 2)
        self.assertEqual(day3.part1(1024), 31)
        self.assertEqual(day3.part2(27), 54)
        self.assertEqual(day3.part2(122), 133)
        self.assertEqual(day3.part2(330), 351)
        self.assertEqual(day3.part2(747), 806)


if __name__ == '__main__':
    unittest.main()
