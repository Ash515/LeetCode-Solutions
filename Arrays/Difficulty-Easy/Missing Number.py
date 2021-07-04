'''
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        total = ((n+1) * n ) // 2
        
        for i in nums:
            total -= i
        return total