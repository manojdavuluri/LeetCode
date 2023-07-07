class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Left pointer ( Increase if uniue element is found) 
        l =1
        # Right pointer ( Scan Through the list)
        for r in range (1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
                
        
        