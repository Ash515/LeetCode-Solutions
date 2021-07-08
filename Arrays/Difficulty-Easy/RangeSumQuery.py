'''
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:

    def __init__(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return (self.nums[right] - self.nums[left-1])