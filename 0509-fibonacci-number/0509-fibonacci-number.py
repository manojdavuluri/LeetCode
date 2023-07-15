class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        i=2
        dp = [0,1]
        while i<=n:
            temp=dp[1]
            dp[1]=dp[0]+dp[1]
            dp[0]=temp
            i+=1
        return dp[1]
 
        
        