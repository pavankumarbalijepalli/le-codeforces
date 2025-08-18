class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        if len(nums)==1:
            return nums[0]
        for num in nums:
            if counter.get(num):
                counter[num] += 1
                if counter[num] > len(nums)//2:
                    return num
            else:
                counter[num] = 1