class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counttext = Counter(text)
        countb = Counter('balloon')
        res = len(text)
        for c in countb:
            res = min(res,counttext[c] // countb[c])
        return res