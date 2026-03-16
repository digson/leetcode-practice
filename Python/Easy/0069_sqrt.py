class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2      
    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(2147395599) == 46339
    print("All test cases passed!")