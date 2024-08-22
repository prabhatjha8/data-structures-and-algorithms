
class TreeNode:
    def __init__(self, val = 0, left = None, right= None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    
    if root == None:
        return []
    
    else:
        return [root.val] + preorder_traversal(root.left) +  preorder_traversal(root.right)


def inorder_traversal(root):
    
    if root == None:
        return []
    
    else:
        return  inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def postorder_traversal(root):
    
    if root == None:
        return []
    
    else:
        return postorder_traversal(root.left) +  postorder_traversal(root.right) + [root.val] 


# Example

root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right = TreeNode(8)
root.right.right = TreeNode(11)

print("preorder of the root: ", preorder_traversal(root))
print("inorder of the root: ", inorder_traversal(root))
print("postorder of the root: ", postorder_traversal(root))
