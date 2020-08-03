#binary search tree implementation in python


class Node(object):
    def __init__(self,val =None):
        self.val= val
        self.right =None
        self.left = None
class Binary_Search_Tree(object):
    def __init__(self,root = None):
        self.root = Node(root)
    
    # public classes 
    def search(self,val):
        return self._search(self.root, val)

    def insert(self,val):
        if self.root == None:
            return Node(val)
        self._insert(self.root,val)

    def display(self):
        self._display(self.root, 0)
        
    
    
    #private classes
    def _insert(self, root, val):
        if val > root.val:  
            if root.right == None:
                root.right = Node(val)
            else:
                return self._insert(root.right ,val )
        else:
            if root.left == None:
                root.left = Node(val)
            else:
                return self._insert(root.left, val )
    
    def _search(self, root, val):
        if root.val == val or root is None:
            return root

        if root.val < val:
            return self._search(root.right,val)
        return self._search(root.left,val)

    def _display(self,root,space):
        if root == None:
            return 
  
        # Increase distance between levels  
        space += 6 

        # Process right child first  
        self._display(root.right, space)  

        for i in range(6, space): 
            print(end = " ")  
        print(root.val)  

        # Process left child  
        self._display(root.left, space)  

if __name__ == '__main__':
    bst = Binary_Search_Tree(15)
    [bst.insert(n) for n in (10,20,8,12,17,25)]
    bst.display()

#redblacktree later