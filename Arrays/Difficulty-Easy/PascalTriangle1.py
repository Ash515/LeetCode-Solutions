'''
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
'''
class Solution:
    def generate(self, numRows):
        pas_tri = [[] for i in range(numRows)]
       
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0:
                    pas_tri[i].append(1)
                elif j == i:
                    pas_tri[i].append(1)
                else:
                    if i > 0:
                        pas_tri[i].append(pas_tri[i-1][j-1] + pas_tri[i-1][j])
        return pas_tri