# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l = float("inf")
        self.r = -1
        
    def GetNumberOfK(self, data, k):
        # write code here
        if not data: return 0
        self.rec(data, 0, len(data), k)
        if self.r >= 0:
            return self.r - self.l + 1
        return 0
    
    def rec(self, data, s, e, k):
        if s==e:
            if data[s]==k: 
                self.l, self.r = min(self.l, s), max(self.r, s)
            else:
                return
        if s >= self.l and e-1 <= self.r: return
        mid = (e - s) // 2 + s
        flag = False
        if data[mid] == k:
            self.l = min(self.l, mid)
            self.r = max(self.r, mid)
            flag = True
        if data[mid] > k or flag:
            self.rec(data, s, mid, k)
        if data[mid] < k or flag:
            if mid+1!=e: self.rec(data, mid+1, e, k)
        print(self.l, self.r)

a = [1,2,3,3,3,3,4,5]
a = [1,2,3,3,3,3]
s = Solution()
import pdb
pdb.set_trace()
res = s.GetNumberOfK(a, 3)
print(res)
