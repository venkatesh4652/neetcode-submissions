class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_to_n = {}
        res = []
        for h,n in zip(heights,names):
            h_to_n[h] = n
        for h in reversed(sorted(heights)):
            res.append(h_to_n[h])
        return res