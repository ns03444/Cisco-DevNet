import math
import unittest


def get_pi(r):
    return r*2*math.pi

class TestMyCode(unittest.TestCase):
     def test_circum_pass(self):
        self.assertEqual(get_pi(5), 31.41592653589793)

     def test_circum_fail(self):
        self.assertEqual(get_pi(1), 31.41592653589793)

# unittest.main()In [3]: path ="C:\Users\19122\Downloads\CBT Nuggets - Devnet Associate\CBT Nuggets - Devnet Associate"
#   Cell In[3], line 1
#     path ="C:\Users\19122\Downloads\CBT Nuggets - Devnet Associate\CBT Nuggets - Devnet Associate"
#                                                                                                   ^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape