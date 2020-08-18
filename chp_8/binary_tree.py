from tree_ABC import Tree

class BinaryTree(Tree):
    def left(self,p):
        '''
            :return: - POSITION of left child
                     - None if non exsistent
        '''
        raise NotImplementedError('must be implemented by subclass')

    def right(self,p):
        '''
            :return: - POSITION of right child
                     - None if non exsistent
        '''
        raise NotImplementedError('must be implemented by subclass')
    
    def siblings(self,p):
        """
            :return: - sibling
                     - None  
        """   
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self,p):
        ''' 
            :yiled: - left child
                    - right child
        '''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def display(self):
        self._display(self.root(), 0)

    def _display(self,root,space):
        if root == None:
            return 
  
        # Increase distance between levels  
        space += 10

        # Process right child first  
        self._display(self.right(root), space)  

        #spacing out values on the same level
        for i in range(10, space): 
            print(end = " ")  
        print(root.element)  

        # Process left child  
        self._display(self.left(root), space) 
