class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[1],nums[0])
        
        rob1, rob2 = 0, 0
        i=0
        while i<len(nums)-1:
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            i+=1
        sol1 = rob2
        
        rob1, rob2 = 0, 0
        i=1
        while i< len(nums):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            i+=1
        sol2 = rob2
        return max(sol1,sol2)