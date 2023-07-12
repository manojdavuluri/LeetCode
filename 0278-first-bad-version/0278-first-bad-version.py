# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 0, n-1    
        while L <= R:
            mid = ( L+R ) // 2
            if isBadVersion(mid) == False:
                L = mid + 1
            else:
                R = mid - 1
        return L
                
                
        