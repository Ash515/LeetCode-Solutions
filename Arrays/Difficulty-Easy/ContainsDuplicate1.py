'''
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums):
        s = set(nums)
        if(len(nums) == len(s)):
            return False
        else:
            return True
        