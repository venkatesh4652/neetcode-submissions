class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsum,maxsum = 1,1
        res = max(nums)
        for n in nums:
            if n == 0:
                minsum,maxsum = 1,1
                continue
            temp = maxsum * n
            maxsum = max(maxsum * n,n,minsum * n)
            minsum = min(minsum * n,n,temp)
            res = max(res,maxsum)
        return res
            