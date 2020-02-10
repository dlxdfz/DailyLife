# -*- coding:utf-8 -*-
import math
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # 1 2 3 4 5 6 = (1 + 6) * (6 - 1 + 1) / 2 = 21
        # (l + r) * (r - l + 1) = 2 * tsum
        if type(tsum) is not int: return []
        if tsum < 1: return []
        res = []
        for i in range(2, int(math.sqrt(2 * tsum))):
            t = self.fun(tsum, i)
            if t: res.append(t)
        return res
        
    def fun(self, n, l):
        if 2 * n % l: return False
        L = 2 * n / l + l - 1
        if L % 2: return False
        L /= 2
        S = 2 * n / l - L
        print(S, L)
        L, S = int(L), int(S)
        return [i for i in range(S, L + 1)]

s = Solution()
print(s.fun(3, 2))
a = 3
res = s.FindContinuousSequence(a)
print(res)
