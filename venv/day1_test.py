import unittest
import day1

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(day1.part1("1122"),"3")
        self.assertEqual(day1.part1("1111"),"4")
        self.assertEqual(day1.part1("1234"),"0")
        self.assertEqual(day1.part1("91212129"),"9")

        self.assertEqual(day1.part2("1212"),"6")
        self.assertEqual(day1.part2("1221"),"0")
        self.assertEqual(day1.part2("123425"),"4")
        self.assertEqual(day1.part2("123123"),"12")


if __name__ == '__main__':
    unittest.main()
