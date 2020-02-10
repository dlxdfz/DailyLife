# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k==0: return []
        if k > len(tinput): return []
        heap = []
        for i in range(k):
            heappush(heap, -tinput[i])
        for n in tinput[k:]:
            if -n > heap[0]:
                heappop(heap)
                heappush(heap, -n)
        heap = [-i for i in heap]
        return sorted(heap)

s = Solution()
res = s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4)
print(res)
