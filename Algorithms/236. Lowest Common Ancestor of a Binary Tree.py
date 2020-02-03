# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path = []
        def PATH(self, a, b):
            if(a == b):
                return True
            if(a.left != None):
                if(PATH(self, a.left, b)):
                    self.path.append(a.left)
                    return True
            if(a.right != None):
                if(PATH(self, a.right, b)):
                    self.path.append(a.right)
                    return True
            return False
            
        
        PATH(self, root, q)
        self.path.append(root)
        qPath = self.path[::-1]
        
        self.path = []
        PATH(self, root, p)
        self.path.append(root)
        pPath = self.path[::-1]
        
        
        LCA = 0
        while(LCA < len(pPath) and LCA < len(qPath) and pPath[LCA] == qPath[LCA]):
            LCA += 1
        return pPath[LCA - 1]
        