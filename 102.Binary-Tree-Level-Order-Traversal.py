class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def build_bt(arr):
    if not arr:
        return None

    index = 1
    root = TreeNode(arr[0])
    queue = [root]
    
    while index<len(arr):
        curr = queue.pop(0)
        if index<len(arr):
            curr.left = TreeNode(arr[index])
            index+=1
            queue.append(curr.left)
            
        else:
            curr.left = TreeNode(None)
                    
        if index<len(arr):
            curr.right = TreeNode(arr[index])
            index+=1
            queue.append(curr.right)
            
        else:
            curr.right = TreeNode(None)

    return root




def print_bt(root):  
    if not root:
        return []
    arr=[]
    inner = []
    queue = [root]
    
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node:
                inner.append(node.val)
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                
        arr.append(inner)
        inner = []
        
    return arr


print(print_bt(build_bt([])))
print(print_bt(build_bt([1])))
print(print_bt(build_bt([1,2,3,4,7])))