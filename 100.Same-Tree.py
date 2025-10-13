class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right
        
        
def build_binary_tree(arr):
    if not arr:
        return None
    
    i = 1
    root = TreeNode(arr[0])
    to_do = [root]
    
    while i < len(arr):
        curr = to_do.pop(0)
        
        curr.left = TreeNode(arr[i])
        i+=1
        to_do.append(curr.left)
        
        curr.right = TreeNode(arr[i])
        i+=1
        to_do.append(curr.right)
        
    return root
        

def isSameTree(p, q):
    if p == None and q == None:
        return True
    
    if p == None or q == None:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    
    
    
p = build_binary_tree([1,2,3])
q = build_binary_tree([1,2,3])
o = build_binary_tree([1,2,4])

print(isSameTree(p, q))
print(isSameTree(p, o))