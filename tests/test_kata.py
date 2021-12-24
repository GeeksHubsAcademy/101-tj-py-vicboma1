import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):

    def test_apply_with_Array_0(self):
        asserted = ['0.0000', '0.0000', '1.0000'] 
        result = apply([0])
        assert(result == asserted)
   

    def test_apply_with_Array_1(self):
        asserted = ["0.0000", "1.0000", "0.0000"] 
        result = apply([-4])
        assert(result == asserted)
   

    def test_apply_with_Array_2(self):
        asserted = ["1.0000", "0.0000", "0.0000"] 
        result = apply([10])
        assert(result == asserted)
   

    def test_apply_with_Array_3(self):
        asserted = ["0.5000", "0.3333", "0.1667"] 
        result = apply([-4, 3, -9, 0, 4, 1])
        assert(result == asserted)
   

    def test_apply_with_Array_4(self):
        asserted = ["0.5000","0.3333", "0.1667"] 
        result = apply([5, -2, -9, 2, 0, 9])
        assert(result == asserted)
   

    def test_apply_with_Array_5(self):
        asserted = ["0.1667","0.1667", "0.6667"] 
        result = apply([0, 0, 0, 10, 0, -8])
        assert(result == asserted)
   

    def test_apply_with_Array_6(self):
        asserted = ["0.0000", "0.6667", "0.3333"] 
        result = apply([-5, -6, -9, -6, 0, 0])
        assert(result == asserted)
   

    def test_apply_with_Array_7(self):
        asserted = ["0.5000","0.5000", "0.0000"] 
        result = apply([5, 2, 9, -2, -2, -9])
        assert(result == asserted)
   

    def test_apply_with_Array_7(self):
        asserted = ["0.3333", "0.3333","0.3333"] 
        result = apply([10, 0, -8])
        assert(result == asserted)
   

if __name__ == '__main__':
	unittest.main()