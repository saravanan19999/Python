import unittest
from calci import add1,subtract,divide,multiply

class LearnTest(unittest.TestCase):


    def setUp(self):
        self.a=20
        self.b=30
    def testsum(self):
        self.assertEqual(add1(self.a,self.b), self.a+self.b)
    def testsubtract(self):
        self.assertEqual(subtract(self.a,self.b), self.a-self.b)
    def testmultiply(self):
        self.assertEqual(multiply(self.a,self.b), self.a*self.b)
    def testdivide(self):
        self.assertEqual(divide(self.a,self.b), self.a/self.b)


if __name__ == '__main__':
    unittest.main()