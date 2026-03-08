class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
if __name__ == "__main__":  
    s = Solution()
    # Test Case 1: Standard case
    assert s.isValid("()") == True
    # Test Case 2: Mixed parentheses
    assert s.isValid("()[]{}") == True
    # Test Case 3: Incorrectly nested parentheses
    assert s.isValid("(]") == False
    # Test Case 4: Empty string
    assert s.isValid("") == True
    print("All test cases passed!")
    