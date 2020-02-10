import os

def DG(A, res):
    if len(A)==0:
        return
    a = A[0]
    B = A[1:]
    res1 = [(a, item) for item in B]
    DG(B, res)
    #res = res + res1
    res.extend(res1)

def DG_n(A, n, res):
    '''
    A的n组合数，结果存放在res中
    '''
    if n < 1:
        return
    if n == 1:
        res.extend([[item] for item in A])
    if len(A) < n:
        return
    for i in range(len(A) - n + 1):
        A_ = A[i+1:]
        res_ = []
        DG_n(A_, n-1, res_)
        for item in res_:
            res.append([A[i]] + item)
        print(res)

if __name__=="__main__":
    A = [i for i in range(10)]
    res = []
    #DG(A, res)
    import pdb
    #pdb.set_trace()
    DG_n(A, 3, res)
    print(res)
    print(len(res))
    print(10*9*8/6)
