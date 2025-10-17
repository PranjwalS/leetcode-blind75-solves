class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
        
def insert(root, val):
    if not val:
        return root
    
    if not root:
        return TreeNode(val)
        
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root
        
def build_bst(arr):
    if not arr:
        return None
    
    root = None
    for val in arr:
        root = insert(root, val)
    
    return root


def lowestCommonAncestor(root, p, q):

    if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
        return root.val

    
    if p.val<root.val and q.val<root.val:
        return lowestCommonAncestor(root.left, p, q)
        
    if p.val>root.val and q.val>root.val:
        return lowestCommonAncestor(root.right, p, q)


        

print(lowestCommonAncestor(build_bst([6,2,8,0,4,7,9,None, None, 3,5]), (build_bst([2])), (build_bst([8]))))
print(lowestCommonAncestor(build_bst([6,2,8,0,4,7,9,None, None, 3,5]), (build_bst([2])), (build_bst([4]))))
print(lowestCommonAncestor(build_bst([2,1]), (build_bst([2])), (build_bst([1]))))