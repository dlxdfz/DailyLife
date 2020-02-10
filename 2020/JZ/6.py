# -*- coding:utf-8 -*-
import functools
def cmp(a, b):
    print(a, b)
    A = str(a) + str(b)
    B = str(b) + str(a)
    if A > B:
        return 1
    elif A < B:
        return -1
    else:
        return 0
    
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ""
        numbers.sort(key=functools.cmp_to_key(cmp))
        print(sorted(numbers, key = functools.cmp_to_key(cmp)))
        res = ""
        for n in numbers:
            res = res + str(n)
        return res

s = Solution()
res = s.PrintMinNumber([5,4,3,2,1])
print(res)
