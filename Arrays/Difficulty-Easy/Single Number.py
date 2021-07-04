'''
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if(nums.count(i)==1):
                return i