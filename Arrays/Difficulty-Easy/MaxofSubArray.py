'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''
class Solution:
    def maxSubArray(self, nums):
        largest = nums[0]
        curr = 0
        for num in nums:
            curr += num
            if curr > largest:
                largest = curr
            if curr < 0:
                curr = 0
        return largest