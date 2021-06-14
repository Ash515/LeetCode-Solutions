'''
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        if m == 0:
            nums1.clear()
            for i in nums2:
                nums1.append(i)
        else:
            i = 0
            j = 0
            k = len(nums1)
            while i < k and j < n:
                if nums2[j] <= nums1[i]:
                    temp = nums1[i]
                    nums1[i] = nums2[j]
                    nums1.insert(i+1, temp)
                    j += 1
                # END If
                i += 1
            # END While
            
            t = n
            while t > 0:
                nums1.pop()
                t -= 1
            # END While
            
            if j < n:
                while j < n:
                    nums1.append(nums2[j])
                    i += 1
                    j += 1