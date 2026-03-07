class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i,column in enumerate(zip(*strs)):
            if len(set(column)) > 1:
                return strs[0][:i]
        return min(strs, key=len)
    
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case
    assert sol.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    
    # Test Case 2: No common prefix
    assert sol.longestCommonPrefix(["dog","racecar","car"]) == ""
    
    # Test Case 3: All strings are the same
    assert sol.longestCommonPrefix(["test","test","test"]) == "test"
    
    # Test Case 4: Empty string in the list
    assert sol.longestCommonPrefix(["","b","c"]) == ""

    print("All test cases passed!")