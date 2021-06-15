'''228. Summary Ranges
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
'''

class Solution:
    def summaryRanges(self, nums):
        
        
        if(nums == []):
            return []
        
        start = str(nums[0])
        
        ans = []
        for i in range(1,len(nums)):
            
            if(nums[i] == nums[i-1]+1):
                continue
            else:
                if(start == str(nums[i-1])):
                    ans.append(start)
                    
                else:
                    ans.append(start+'->'+str(nums[i-1]))
                start = str(nums[i])
        
        if(start == str(nums[-1])):
            ans.append(str(nums[-1]))
            
        else:
            ans.append(start+'->'+str(nums[-1]))
            
        return ans