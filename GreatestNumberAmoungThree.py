import unittest

def greatestNumberofThree(a,b,c):
    #print("Given number a = ",a,"b = ",b,"c = ",c)
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(greatestNumberofThree(5,10,3),10)
    def test2(self):
        self.assertEqual(greatestNumberofThree(100,200,150),200)
    def test3(self):
        self.assertEqual(greatestNumberofThree(100,100,50),100)
if __name__ == '__main__':
    unittest.main()
