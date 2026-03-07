class Solution(object):
    def romanToInt(self, s):
        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        
        for i in range(len(s)):
            # If there is a next character AND it is larger than the current one
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
                total -= mapping[s[i]]
            else:
                total += mapping[s[i]]
                
        return total
    
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case
    assert sol.romanToInt("III") == 3
    
    # Test Case 2: Subtractive notation
    assert sol.romanToInt("IV") == 4
    
    # Test Case 3: Mixed notation
    assert sol.romanToInt("MCMXCIV") == 1994
    
    # Test Case 4: Single character
    assert sol.romanToInt("L") == 50

    print("All test cases passed!")