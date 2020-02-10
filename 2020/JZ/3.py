# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead: return None
        p = pHead
        res = RandomListNode(0)
        p1 = res
        while p:
            p1.next = RandomListNode(p.label)
            p = p.next
            p1 = p1.next
        # last k
        p = pHead
        p1 = res.next
        while p:
            if p.random:
                r = p.random
                k = 0
                while r:
                    k += 1
                    r = r.next
                ptf, pts = res.next, res.next
                for i in range(k):
                    ptf = ptf.next
                while ptf:
                    ptf = ptf.next
                    pts = pts.next
                p1.random = pts
            p = p.next
            p1 = p1.next
        return res.next

    def Clone1(self, pHead):
        # write code here
        if not pHead: return None
        # state 1 copy
        p = pHead
        while p:
            cn = RandomListNode(p.label)
            tp = p.next
            p.next = cn
            cn.next = tp
            p = tp
        # state 2 link random
        p = pHead
        while p:
            if not p.random:
                p = p.next.next
                continue
            p.next.random = p.random.next
            p = p.next.next
        # state 3 split
        p = pHead
        res = pHead.next
        while p.next:
            cp = p.next
            p.next = cp.next
            p = cp
        return res

if __name__=="__main__":
    def P(head):
        res1 = []
        res2 = []
        while head:
            res1.append(head.label)
            if head.random:
                res2.append(head.random.label)
            else:
                res2.append('#')
            head = head.next
        print(res1)
        print(res2)
    nodes = [RandomListNode(i) for i in range(4)]
    head = nodes[0]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    nodes[0].random = nodes[2]
    nodes[1].random = nodes[3]
    P(head)

    import pdb
    pdb.set_trace()
    s = Solution()
    res = s.Clone(head)
    P(head)
