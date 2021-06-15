'''169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
class Solution:
    def majorityElement(self, a):
        new=[]
        index=[]
        val=[]
        a_cpy=[a[x] for x in range(len(a)) ]
        sets=set(a_cpy)
        lis=list(sets)
        for i in range(len(lis)):
            x=a.count(lis[i])
            new.append(lis[i])
            new.append(x)
        for k in range(1,len(new),2):
            index.append(new[k-1])
            val.append(new[k])
        m=max(val)
        index_val=val.index(m)
        for g in range(len(index)):
            g=index_val
        return(index[g])