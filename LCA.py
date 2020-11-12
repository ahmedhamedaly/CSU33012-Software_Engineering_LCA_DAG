# Code adapted from geeksforgeeks.org

class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def lca(root, n1, n2): 

    if not isinstance(n1, int) or not isinstance(n2, int) or root is None:
        return None
  
    if root.data > n1 and root.data > n2: 
        return lca(root.left, n1, n2) 
 
    if root.data < n1 and root.data < n2: 
        return lca(root.right, n1, n2) 
  
    return root   