class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n
        
        prod = 1
        for i in range(1, n):
            prod *= nums[i-1]
            out[i] *= prod

        prod = 1
        for i in range(n - 2, -1 , -1):
            prod *= nums[i+1]
            out[i] *= prod
        
        return out