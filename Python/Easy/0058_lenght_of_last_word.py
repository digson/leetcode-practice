class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1]) if words else 0
if __name__ == "__main__":
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert Solution().lengthOfLastWord("luffy is still joyboy") == 6

    print("All test cases passed!")
        