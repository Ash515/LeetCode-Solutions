'''
122. Best Time to Buy and Sell Stock II
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
             
        return profit
             