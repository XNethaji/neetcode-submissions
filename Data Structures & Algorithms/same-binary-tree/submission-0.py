# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = []
        res1=[]

        a = deque([p])

        while a:
            node = a.popleft()
            if node :
                res.append(node.val)
                a.append(node.left)
                a.append(node.right)
            else:
                res.append('null')

        b= deque([q])

        while b:
            node = b.popleft()
            if node :
                res1.append(node.val)
                b.append(node.left)
                b.append(node.right)
            else:
                res1.append('null')
        
        return res == res1
       