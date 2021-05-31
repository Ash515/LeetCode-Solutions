'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        elif target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        
        