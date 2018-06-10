from textFunc import sub,sum
from testClass import myFriends
import unittest


class FuncTest(unittest.TestCase):
    def setUp(self):
        print("开始测试。。。。。。。")
    def tearDown(self):
        print("结束测试。。。。。。。")

    def test_sum(self):
        self.assertEqual(sum(1,2),3,"加法错误")

    def test_sub(self):
        self.assertEqual(sub(2,1),1,"减法错误")

class testClass(unittest.TestCase):
    def setUp(self):
        print("Class开始测试.....")
    def tearDown(self):
        print("Class结束测试........")
    #test_前缀一定要加，否则它不会测试
    def test_Age(self):
        c=myFriends("ping",20)
        self.assertEqual(c.mName,"ping","名字都打错，笨~")
    def test_GetAge(self):
        c = myFriends("ping", 22)
        self.assertEqual(c.getAge(),c.mAge,"函数错了")





if __name__=="__main__":
    unittest.main()