# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        print(sequence)
        if not sequence: return True
        if len(sequence)==1: return True
        root = sequence[-1]
        for i, val in enumerate(sequence[:-1]):
            if val > root: break
        if i==len(sequence[:-1])-1:
            return True
        for j in range(i, len(sequence)-1):
            if sequence[j] < root: return False
        return self.VerifySquenceOfBST(sequence[:i]) and self.VerifySquenceOfBST(sequence[i:-1])


if __name__ == "__main__":
    import pdb
    pdb.set_trace()
    s = Solution()
    #res = s.VerifySquenceOfBST([4, 6, 7, 5])
    res = s.VerifySquenceOfBST([5,4,3,2,1])
    #res = s.VerifySquenceOfBST([6,7])
    print(res)
