# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = [root]
        path_q = [root]
        
        curr = root
        while(curr != p):
            if(p.val > curr.val):
                curr = curr.right
            else:
                curr = curr.left
            path_p.append(curr)
        
        curr = root
        while(curr != q):
            if(q.val > curr.val):
                curr = curr.right
            else:
                curr = curr.left
            path_q.append(curr)
        
        indx = 0
        Lp = len(path_p)
        Lq = len(path_q)
        
        while(indx < Lp and indx < Lq and path_p[indx] == path_q[indx]):
            indx += 1
            
        return path_p[indx - 1]
        