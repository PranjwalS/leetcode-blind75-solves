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
    root = None
    for val in arr:
        root = insert(root, val)
    return root



def kthSmallest(root, k):
    state = [0, None]
    
    def compare(root, k, state):
        if not root:
            return
        
        compare(root.left, k, state)
        state[0] +=1
        if state[0] == k:
            state[1] = root.val

            
        compare(root.right, k, state)
        return state[1]
    
    result = compare(root, k, state)
    return result

    

print(kthSmallest(build_bst([5,3,7]), 3))
print(kthSmallest(build_bst([5,3,6,2,4,None, None, 1]), 1))
