class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min,cur_max = arrays[0][0],arrays[0][-1]
        res = 0
        for i in range(1,len(arrays)):
            arr = arrays[i]
            res = max(res,max(cur_max - arr[0],arr[-1] - cur_min))
            cur_min = min(arr[0],cur_min)
            cur_max = max(arr[-1],cur_max)
        return res