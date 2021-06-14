'''
66. Plus One
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
class Solution:
    def plusOne(self, digits):
        
        b=[str(i) for i in digits]
        c="".join(b)
        c=int(c)
        c+=1
        d=[str(x) for x in str(c)]
        e=[int(y) for y in d]
        return(e)
    
 


        
        
        