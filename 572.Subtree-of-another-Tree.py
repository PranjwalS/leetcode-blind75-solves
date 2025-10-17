class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        
        
def build_tree(arr):
    if not arr:
        return None
    root= TreeNode(arr[0])
    to_do = [root]
    index = 1
    
    
    while index<len(arr):
        curr = to_do.pop(0)
        
        if index<len(arr):
            curr.left = TreeNode(arr[index])
            index +=1
            to_do.append(curr.left)
        else:
            curr.left = None
            
        if index<len(arr):
            curr.right = TreeNode(arr[index])
            index +=1
            to_do.append(curr.right)
        else:
            curr.right = None
            
    return root




def isSameTree(root,subRoot):
    if root is None and subRoot is None:
        return True

    if root is None or subRoot is None:
        return False
    
    
    if root.val != subRoot.val:
        return False
    
    return (isSameTree(root.left, subRoot.left)) and (isSameTree(root.right, subRoot.right))


def isSubtree(root, subRoot):
    if not root or not subRoot:
        return False
    
    if isSameTree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot):
        return True

    return False
    
    
        
    

print(isSubtree(build_tree([3,4,5,1,2]), build_tree([5,1,2])))
    
    
    
    
    


def print_binary_tree(root):
    if not root:
        return
    arr = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            arr.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return arr
    
