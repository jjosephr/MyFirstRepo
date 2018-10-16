import unittest


def factorial(x):
    if x == 1 or x == 0:
        return 1
    elif x<1:
        return "Not possible"
    else:
        x = x * factorial(x-1)
    return x


class UnitTest(unittest.TestCase):
    def test1(self):
        #print(factorial(10)) #3628800
        self.assertEqual(factorial(10),3628800)
    def test2(self):
        #print(factorial(5))
        self.assertEqual(factorial(5),120)
    def test3(self):
        #print(factorial(-10))
        self.assertEqual(factorial(-10),"Not possible")
    def test4(self):
        #print(factorial(5))
        self.assertEqual(factorial(0), 1)
    def test5(self):
        #print(factorial(5))
        self.assertEqual(factorial(1), 1)

if __name__ == '__main__':
    unittest.main()



