# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2**x.

import time

# Official solutions
class Solution2(object):
    def isPowerOfTwo(self, n):
        if(n<=0):
            return False; 
        if((n&n-1)==0):
            return True; 
        return False;

# Test:
solu = Solution2()
t0 = time.time()
print(solu.isPowerOfTwo(15))
print(solu.isPowerOfTwo(16))
print(solu.isPowerOfTwo(1))
official_time = time.time() - t0
print(official_time)


# My solutions
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math

        while(n>=2):
            n = n / 2.0
            # print(n)
            if not math.floor(n) == n:
                return False

        if n==1:           
            return True
        
        return False


solu = Solution()
t0 = time.time()
print(solu.isPowerOfTwo(15))
print(solu.isPowerOfTwo(16))
print(solu.isPowerOfTwo(1))
my_time = time.time() - t0
print(my_time)
print('My time cost is {:.2f} times as the official cost.'.format(my_time/official_time))