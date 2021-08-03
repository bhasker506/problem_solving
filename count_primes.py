import math

class Solution:
    
    def countPrimes(self, n: int) -> int:
        
        if n<2:
            return 0
        
        #initialize a list of length n
        prime=[1]*n
		#mark 0th  and 1st index as 0
        prime[0]=prime[1]=0
        
        p = 2
		#we will check for multiple from range 2 to sqrt(n)
        while p*p < n:
            if prime[p] == 1:
                #mark all multiple of prime number as  0
                j = 2
                while j*p < n:
                    prime[j*p] = 0
                    j += 1
            p += 1		    
    #return total count of prime 
        return sum(prime)

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))
            