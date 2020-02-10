class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BT(object):
    def __init__(self, pre, tin):
        self.root = self.build(pre, tin)

    def build(self, pre, tin):
        if not pre:
            return None
        root_val = pre[0]
        for i, val in enumerate(tin):
            if root_val == val:
                root_ind = i
        root = Node(root_val)
        root.left = self.build(pre[1:root_ind+1], tin[:root_ind])
        root.right = self.build(pre[root_ind+1:], tin[root_ind+1:])
        return root

    def qx(self, root):
        if not root:
            return
        print(root.val, end=',')
        self.qx(root.left)
        self.qx(root.right)

    def qx1(self):
        if not self.root:
            return
        s = [self.root]
        while s:
            n = s.pop()
            print(n.val, end=',')
            if n.right: s.append(n.right)
            if n.left: s.append(n.left)
        print(' ')

    def zx(self, root):
        if not root:
            return
        self.zx(root.left)
        print(root.val, end=',')
        self.zx(root.right)

    def zx1(self):
        if not self.root:
            return
        s = []
        root = self.root
        while root:
            s.append(root)
            root = root.left
        while s:
            n = s.pop()
            print(n.val, end=',')
            root = n.right
            while root:
                s.append(root)
                root = root.left
        print(' ')

    def hx(self, root):
        if not root:
            return
        self.hx(root.left)
        self.hx(root.right)
        print(root.val, end=',')

    def hx1(self):
        if not self.root:
            return
        res = []
        s = [self.root]
        while s:
            n = s.pop()
            res.append(n.val)
            if n.left: s.append(n.left)
            if n.right: s.append(n.right)
        for val in res[::-1]:
            print(val, end=',')
        print(' ')

    def cx(self):
        if not self.root:
            return
        q = [self.root]
        while q:
            n = q.pop(0)
            print(n.val, end=',')
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        print(' ')

    def copy_base(self, root):
        if not root:
            return None
        root_copy = Node(root.val)
        root_copy.left = self.copy_base(root.left)
        root_copy.right = self.copy_base(root.right)
        return root_copy
    
    def copy(self):
        root = self.copy_base(self.root)
        bt = BT([], [])
        bt.root = root
        return bt

    def mirror_base(self, root):
        if not root: return None
        mir = Node(root.val)
        mir.left = self.mirror_base(root.right)
        mir.right = self.mirror_base(root.left)
        return mir

    def mirror(self):
        mir = self.mirror_base(self.root)
        bt = BT([], [])
        bt.root = mir
        return bt

    def depth_base(self, root, level=0):
        if not root:
            return level
        l = self.depth_base(root.left, level=level+1)
        r = self.depth_base(root.right, level=level+1)
        return max(l, r)

    def depth(self):
        return self.depth_base(self.root, level=0)

if __name__=="__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    bt = BT(pre, tin)
    bt.qx(bt.root)
    print(' ')
    bt.qx1()
    bt.zx(bt.root)
    print(' ')
    bt.zx1()
    bt.hx(bt.root)
    print(' ')
    bt.hx1()

    bt.cx()

    bt_copy = bt.copy()
    bt_copy.cx()

    d = bt_copy.depth()
    print(d)

    mir = bt.mirror()
    mir.qx1()
