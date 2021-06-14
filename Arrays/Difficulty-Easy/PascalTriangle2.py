'''
119. Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
class Solution:
	def getRow(self, rowIndex):
		x=[]
		y=[[1]]
		if rowIndex<1:
			return(y[-1])
		for i in range(1,rowIndex+1):
			x.append(1)
			for j in range(1,len(y[-1])):
				a=y[-1]
				if i>1:
					x.append(a[j-1]+a[j])
			x.append(1)
			y.append(x)
			x=[]
		return(y[-1])
    
    
    