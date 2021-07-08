'''
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
'''
class Solution:
    def intersection(self, a, b):
        new=[]
        for i in b:
            if( i in a):
                new.append(i)
        d=list(set(new))
        return d
        