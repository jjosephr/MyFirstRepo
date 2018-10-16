import unittest

def EvenOdd(v):
    if (v%2 == 0):
        return "Even"
    else:
        return "Odd"

class EvenOddTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(EvenOdd(10),"Even")
    def test2(self):
        self.assertEqual(EvenOdd(11),"Odd")
    def test3(self):
        self.assertEqual(EvenOdd(0),"Even")
    def test4(self):
        self.assertEqual(EvenOdd(-10),"Even")

if __name__ == '__main__':
    unittest.main()


