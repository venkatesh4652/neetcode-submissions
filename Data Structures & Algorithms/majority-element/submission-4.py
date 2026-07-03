class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxcount = 0
        for n in nums:
            count[n] += 1
            if maxcount < count[n]:
                maxcount = count[n]
                res = n
        return res