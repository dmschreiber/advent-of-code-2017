import unittest
import time
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22

class MyTestCase(unittest.TestCase):
    # def test_day4(self):
    #     self.assertEqual(day4.part2_validate("iiii oiii ooii oooi oooo"), True)
    #     self.assertEqual(day4.part2_validate("oiii ioii iioi iiio"), False)
    #     self.assertEqual(day4.part2_validate("abcde fghij"), True)
    #     self.assertEqual(day4.part2_validate("abcde xyz ecdab"), False)
    #
    # def test_day5(self):
    #     input = "./data/day5_test.txt"
    #     self.assertEqual(day5.part1(input),5)
    #     self.assertEqual(day5.part2(input),10)
    #
    # def test_day6(self):
    #     input = "0 2 7 0"
    #     self.assertEqual(day6.redistribute(input),"2 4 1 2")
    #     self.assertEqual(day6.redistribute("2 4 1 2"),"3 1 2 3")
    #     self.assertEqual(day6.redistribute("3 1 2 3"),"0 2 3 4")
    #     self.assertEqual(day6.redistribute("0 2 3 4"),"1 3 4 1")
    #     self.assertEqual(day6.redistribute("1 3 4 1"),"2 4 1 2")
    #     self.assertEqual(day6.part1(input),5)
    #     self.assertEqual(day6.part2(input),4)
    #
    # def test_day7(self):
    #     input = "./data/day7_test.txt"
    #     self.assertEqual(day7.part1(input),"tknk")
    #     # self.assertEqual(day7.part2(input),60)
    #
    # def test_day8(self):
    #     input = "./data/day8_test.txt"
    #     self.assertEqual(day8.part1(input),1)
    #     self.assertEqual(day8.part2(input),10)
    #
    # def test_day9(self):
    #     self.assertEqual(day9.score("{}"),1)
    #     self.assertEqual(day9.score("{{{}}},"),6)
    #     self.assertEqual(day9.score("{{},{}}"),5)
    #     self.assertEqual(day9.score("{{{},{},{{}}}}"),16)
    #     self.assertEqual(day9.score("{<a>,<a>,<a>,<a>}"),1)
    #     self.assertEqual(day9.score("{{<ab>},{<ab>},{<ab>},{<ab>}}"),9)
    #     self.assertEqual(day9.score("{{<!!>},{<!!>},{<!!>},{<!!>}}"),9)
    #     self.assertEqual(day9.score("{{<a!>},{<a!>},{<a!>},{<ab>}}"),3)
    #
    #     self.assertEqual(day9.score("<!!!>>", False),0)
    #     self.assertEqual(day9.score("<{o\"i!a,<{i<a>", False),10)
    #
    # def test_day10(self):
    #     self.assertEqual(day10.part1("3,4,1,5",5),12)
    #     self.assertEqual(day10.get_part2_lengths("1,2,3"),[49,44,50,44,51,17, 31, 73, 47, 23])
    #     nums = [    65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]
    #     self.assertEqual(day10.sparce_hash(nums),64)
    #     self.assertEqual(day10.part2("1,2,3",256),"3efbe78a8d82f29979031a4aa0b16a9d")
    #
    # def test_day11(self):
    #     home = day11.PointHex(0,0)
    #
    #     self.assertEqual(day11.part1("ne,ne,ne"),3)
    #     self.assertEqual(day11.part1("se,sw,se,sw,sw"),3)
    #     self.assertEqual(day11.part1("se,sw,se,sw,sw"),3)
    #
    # def test_day12(self):
    #     input = "./data/day12_test.txt"
    #     self.assertEqual(day12.part1(input),6)
    #     self.assertEqual(day12.part2(input),2)
    #
    # def test_day13(self):
    #     input = "./data/day13_test.txt"
    #     self.assertEqual(day13.part1(input),24)
    #     start_time = time.perf_counter()
    #     self.assertEqual(day13.part2(input),10)
    #     end_time = time.perf_counter()
    #     # print(f"Day 13 execution Time : {end_time - start_time:0.6f}s")
    #
    # def test_day14(self):
    #     input = "flqrgnkx"
    #     self.assertEqual(day14.part1(input),8108);
    #     self.assertEqual(day14.part2(input),1242)
    #
    # def test_day15(self):
    #     self.assertEqual(day15.part1(65,8921,5),1)
    #     start_time = time.perf_counter()
    #     self.assertEqual(day15.part1(65, 8921, 40000000), 588)
    #     end_time = time.perf_counter()
    #     print(f"Day 15 execution Time : {end_time - start_time:0.6f}s")
    #     self.assertEqual(day15.part2(65, 8921, 1057), 1)
    #     start_time = time.perf_counter()
    #     self.assertEqual(day15.part2(65, 8921, 5000000), 309)
    #     end_time = time.perf_counter()
    #     print(f"Day 15 execution Time : {end_time - start_time:0.6f}s")

    def test_day16(self):
        l = day16.ProgramGroup(5)
        self.assertEqual(l.list(),"abcde")
        l.spin(1)
        self.assertEqual(l.list(),"eabcd")
        l.exchange(3,4)
        self.assertEqual(l.list(), "eabdc")
        l.partner("e","b")
        self.assertEqual(l.list(), "baedc")

    def test_day17(self):
        start_time = time.perf_counter()
        self.assertEqual(day17.part1(2017,2017,3),638)
        end_time = time.perf_counter()
        print(f"Day 17 p1 execution Time : {end_time - start_time:0.6f}s")
        start_time = time.perf_counter()
        self.assertEqual(day17.part2(2017,2017,3),638)
        end_time = time.perf_counter()
        print(f"Day 17 p2 execution Time : {end_time - start_time:0.6f}s")

    def test_day18(self):
        input = "./data/day18_test.txt"

        self.assertEqual(day18.part1(input),4)

        input = "./data/day18_test2.txt"
        self.assertEqual(day18.part2(input),3)

    def test_day19(self):
        input = "./data/day19_test.txt"
        self.assertEqual(day19.part1(input),"ABCDEF")
        self.assertEqual(day19.part2(input), 38)

    def test_day20(self):
        input = "./data/day20_test.txt"
        day20.part2(input)

    def test_day21(self):
        input = "./data/day21_test.txt"
        self.assertEqual(day21.part1(input, 2),12)

        # pattern = day21.starting_pattern
        # self.assertTrue(day21.compare(pattern,day21.rotate2(day21.rotate2(day21.rotate2(day21.rotate2(pattern))))))
        # self.assertTrue(day21.compare(pattern,day21.flip(day21.flip(pattern))))
        # self.assertTrue(day21.compare(pattern,day21.flip2(day21.flip2(pattern))))
        # self.assertTrue(day21.compare(pattern,day21.rotate(day21.rotate(pattern))))
        # self.assertTrue(False== day21.compare(pattern,day21.rotate2(pattern)))

    def test_day22(self):
        input = "./data/day22_test.txt"
        self.assertEqual(day22.move((0,0),90),(0,1))
        self.assertEqual(day22.move((0,0),270),(0,-1))

        self.assertEqual(day22.part1(input,70),41)
        self.assertEqual(day22.part2(input,100),26)
        self.assertEqual(day22.part2(input,10000000),2511944)

if __name__ == '__main__':
    unittest.main()
