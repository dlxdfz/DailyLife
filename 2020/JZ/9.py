# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2: return None
        f1, L1, p1 = self.hasLoop(pHead1)
        f2, L2, p2 = self.hasLoop(pHead2)
        if f1 or f2: return None
        if p1 != p2: return None
        p1, p2 = pHead1, pHead2
        if L1 < L2: p1, p2 = p2, p1
        for _ in range(abs(L1-L2)): p1 = p1.next
        for _ in range(L1):
            if p1==p2: return p1
            p1 = p1.next
            p2 = p2.next
        return None
    
    def hasLoop(self, p):
        if not p: return False, 0, None
        L = 0
        f, s = p, p
        t = f
        while f:
            t = f
            f = f.next
            L += 1
            if f:
                t = f
                f = f.next
                L += 1
            if s:
                s = s.next
            if s==f: return True, L, s
        return False, L, t

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2: return None
        p1, p2 = pHead1, pHead2
        while p1!=p2:
            #p1 = p1.next if p1.next else pHead2
            #p2 = p2.next if p2.next else pHead1
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1

a1 = [ListNode(i) for i in range(10)]
a2 = [ListNode(i) for i in range(5)]
pHead1 = a1[0]
pHead2 = a2[0]
p1, p2 = pHead1, pHead2
for n in a1[1:]:
    p1.next = n  
    p1 = p1.next
for n in a2[1:]:
    p2.next = n  
    p2 = p2.next
#p2.next = a1[5]
p2.next = a1[2]
s = Solution()
import pdb
pdb.set_trace()
res = s.FindFirstCommonNode(pHead1, pHead2)
print(res.val)
