class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevsum = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevsum:
                return [prevsum[diff],i]
            prevsum[n] = i
        return
