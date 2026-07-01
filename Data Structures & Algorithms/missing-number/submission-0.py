class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = sum(nums)
        intendedsum = n * (n + 1) // 2
        return int(intendedsum - totalsum)