class Tree:
    class Position:
    #-------------------- ~ nested Position class ~ -------------------- 
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self,other):
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self,other):
            return not ( self == other)
    #----- abstract methods that concrete class should support ~ -----    
    def root(self):
        '''returns the position representing the trees root'''
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        ''' Returns Position representing ps parent (or NOne if p is root)'''
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self,p):
        ''' Generate an iteration of Positions representing p's children '''
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self,p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self,p):
        ''' returns True if the Position is the root '''
        return self.root() == p
        
    def is_leaf(self,p):
        return self.num_children(p) == 0

    def is_empty(self):
        ''' Return True if the tree is empty'''
        return len(self) == 0
