class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left=left
        self.right = right
        
        
def build_binary_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    index = 1
    to_do = [root]
    
    while index<len(arr):
        curr = to_do.pop(0)
        
            
        if index < len(arr):
            curr.left = TreeNode(arr[index])
            to_do.append(curr.left)
            index += 1
        else:
            curr.left = TreeNode(None)
            
        if index < len(arr):
            curr.right = TreeNode(arr[index])
            to_do.append(curr.right)
            index += 1
        else:
            curr.right = TreeNode(None)
            
    return inverseTree(root)

def inverseTree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left
    inverseTree(root.left)
    inverseTree(root.right)
    return print_tree(root)


def print_tree(root):
    if root is None:
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
    


print(build_binary_tree([4,2,7,1,3,6,9]))
print(build_binary_tree([1,2]))