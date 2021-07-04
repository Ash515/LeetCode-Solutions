'''
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        if n <= 2:
            return 0
        
        total = 0
        primes = [False for i in range(n+1)]
        for i in range(2, n):
            if primes[i] == False:
                total += 1
                j = 2
                while i*j < n:
					#update list primes for flag not primes, eg : 4,6,8 ... n
                    primes[i*j] = True
                    j += 1
        return total