import unittest
import sys

#function
def convert(f, target='c'):
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')

#unittest
class TestDivide(unittest.TestCase):
    def test_wrong_conv_50(self):
        for (f, c) in ((50,10),(70,21.1111111),(90,32.2222222)):
                       self.assertAlmostEqual(convert(f,'c'),c)

    def test_wrong_scale(self):
        with self.assertRaises(Exception): #namefrom raise in function
            convert(1,('c', 'k'))
        
if __name__ == '__main__':
    unittest.main()
