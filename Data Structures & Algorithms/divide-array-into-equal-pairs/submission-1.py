class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for n,cnt in count.items():
            if cnt % 2:
                return False
        return True