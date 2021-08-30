'''
1299. Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.
'''
class Solution:
    def replaceElements(self, arr):
        b=[]
        c=[]
        n=arr[-1]
        for i in range(len(arr)):
            a=arr[i+1:]
            b.append(a)
        b.pop()
        for i in b:
            v=max(i)
            c.append(v)
        c.append(-1)
        return c


        
        
        