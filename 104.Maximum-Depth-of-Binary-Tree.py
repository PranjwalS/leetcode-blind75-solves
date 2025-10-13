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
        
                
        
def maxDepth(root):
    if root == None:
        return 0
    leftdepth = maxDepth(root.left)
    rightdepth = maxDepth(root.right)
    
    return 1 + max(leftdepth, rightdepth)




root = build_binary_tree([3,9,20,None, None,15,7])
print(root.left.left.val)
print(maxDepth(root))
