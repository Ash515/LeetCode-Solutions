#1. Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
class Solution:
    def twoSum(self,nums, target):
        if len(nums) < 2:
            pass
        tempDict = {nums[0] : 0}
        for i in range(1, len(nums)):
            checkNum = target-nums[i]
            if(checkNum in tempDict.keys()):
                return [i,tempDict[checkNum]]
            else:
                tempDict[nums[i]] = i