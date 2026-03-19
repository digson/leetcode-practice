class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1
if __name__ == "__main__":
    s =Solution()
    assert s.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]