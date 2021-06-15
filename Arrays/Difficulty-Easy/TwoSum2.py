'''
167. Two Sum II - Input array is sorted
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''
class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in numbers:
                num = numbers[i+1:]
                return([i+1,num.index(t) + i + 2])
            else:
                pass