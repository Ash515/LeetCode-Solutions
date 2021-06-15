'''
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        freq={}
        for i in range(len(nums)): 
            if nums[i] in freq:
                if i-freq[nums[i]] <= k: 
                    return True
                freq[nums[i]]=i
            else: 
                freq[nums[i]]=i
        return False