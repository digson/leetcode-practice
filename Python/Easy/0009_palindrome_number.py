class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard palindrome
    assert sol.isPalindrome(121) == True
    
    # Test Case 2: Negative number
    assert sol.isPalindrome(-121) == False
    
    # Test Case 3: Number with trailing zero
    assert sol.isPalindrome(10) == False
    
    # Test Case 4: Single digit number
    assert sol.isPalindrome(7) == True

    print("All test cases passed!")       