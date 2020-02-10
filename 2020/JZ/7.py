# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1: return 0
        res = [1]
        p2, p3, p5 = 0, 0, 0
        for _ in range(1, index):
            un2 = res[p2] * 2
            un3 = res[p3] * 3
            un5 = res[p5] * 5
            min_un = min(min(un2, un3), un5)
            if min_un==un2 or (p2 and min_un%res[p2]==0):
                p2 +=1
            if min_un==un3 or (p3 and min_un%res[p3]==0):
                p3 += 1
            if min_un==un5 or (p5 and min_un%res[p5]==0):
                p5 += 1
            res.append(min_un)
            print(res, p2, p3, p5)
        return res[index-1]

s = Solution()
s.GetUglyNumber_Solution(10)
