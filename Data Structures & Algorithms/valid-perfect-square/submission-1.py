class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        while l <= r:
            mid = (l + r) // 2
            sqrt = mid * mid
            if sqrt > num:
                r = mid - 1
            elif sqrt < num:
                l = mid + 1
            else:
                return True
        return False