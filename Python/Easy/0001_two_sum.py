class Solution(object):
    def twoSum(self, nums, target):
        x = {} 
        
        for i, val in enumerate(nums):
            y = target - val
            
            if y in x:
                return [x[y], i]

            x[val] = i

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test Case 2: Numbers are not at the start
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test Case 3: Same number values, different indices
    assert sol.twoSum([3, 3], 6) == [0, 1]
    
    # Test Case 4: Negative numbers
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

    print("All test cases passed!")