from .binary_tree import BinaryTree
class Queue:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self,element,next_= None):
            self._element = element 
            self._next = next_
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0

    def enqueue(self,value):
        node = self._Node(value)
        if self.is_empty():
            # print(f'here\'s what got entered{value}')
            self._head = node 
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('The list is empty')
        temp = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return temp
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""
    class _Node:
        def __init__(self,element,parent= None, left = None, right = None):
            self._element = element 
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            '''
                :NOTE: should not be invoke by user
            '''
            self._container = container 
            self._node = node
        @property
        def element(self):
            '''
                :return: - element stored in node abstraction
            '''
            return self._node._element
        
        def __eq__(self,other):
            return type(other) is type(self) and self.element is other.element
        
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position Type')
        if p._container is not self:
            raise ValueError('P does not belong to this container')
        if p._node._parent is p._node:                                                # convetion for deprecating values
            raise ValueError('value has been deprecated')
        return p._node
    
    def _make_position(self,node):
        '''
            :return: - Position instance for give node
        '''
        return self.Position(self,node) if node is not None else None

#-------------------------- binary tree constructor --------------------------
    def __init__(self):
        self._root = None
        self._size = 0
    def __len__(self):
        return self._size
    
    def root(self):
        '''
            :return: - the root of a tree
        '''
        return self._make_position(self._root)

    def parent(self,p):
        ''' :POSITION p: a position 
            :return: - the parent node
        '''
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self,p):
        '''
            :POSITION p: a position 
            :return: - the left node
        '''
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        '''
            :POSITION p: a position 
            :return: - the right node
        '''
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self,p):
        '''
            :POSITION p: a position 
            :return: - 1 or depending 
        '''
        node = self._validate(p)
        if node._right is not None:
            if node._right is not None:
                return 2
            return 1 
            
    def _add_root(self,e):
        '''
            :POSITION e: sends an element to be made into the root
            :return: - Node wrapped in "Position" class
        '''
        if self._root is not None: raise ValueError('Root exists')
        self._size += 1 
        self._root = self._Node(e)
        return self._make_position(self._Node)
    
    def _add_right(self,p,e):
        '''
            :POSITION e: sends an element to made into the right child
            :return: - Node wrapped in "Position" class
        '''
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        node._right = self._Node(e)
        self._size += 1 
        return self._make_position(node._right)

    def _add_left(self,p,e):
        '''
            :POSITION e: sends an element to be made into the left child
            :return: - Node wrapped in "Position" class
        '''
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left chlid exists')
        node._left = self._Node(e)
        self._size += 1 
        return self._make_position(node._left)

    def _replace(self,p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self,p):
        #validate position turn into node to be deprecated
        node = self._validate(p)

        #limitataion delete function does not support node with two children
        if self.num_children(p) == 2:raise ValueError('This parent has two children')
        
        #compound statement to get child node OR None incase no child node
        child = node._left if node._left else node._right
        
        if child is not None:
            child._parent = node._parent # grandparent becomes the parent
        #make the root the child node
        if node is self._root:
            self._root = child
        #adjust the pointer on the grandparent to point to the child instead of the deprecated node
        else:
            parent = node._parent
            if node == parent.__right:
                parent._right = child
            else:
                parent._left = child
        self._size -= 1
        node._parent = node # convention for deprecated node
    
    def _attach(self,p,t1,t2):
        node = self._validate(p)
        # if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(self):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root 
            t1._root =  None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None 
            t2._size = 0
    def positions(self):
        return self.preorder()

    def __iter__(self):
        for p in self.positions():
            yield p.element

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    
    def _subtree_preorder(self,p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def breadth_first(self):
        if not self.is_empty():
            Q = Queue()
            Q.enqueue(self.root())
            while not Q.is_empty():
                p = Q.dequeue()
                yield p
                for c in self.children(p):
                    Q.enqueue(c) 

    def postorder(self):
        if not self.is_empty():
            for n in self._subtree_postorder(self.root()):
                yield n

    def _subtree_postorder(self,p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p 
    
    def inorder(self):
        if self.is_empty():
            raise ValueError('the tree is empty')

        for p in self._subtree_inorder(self.root()):
            yield p 

    def _subtree_inorder(self,p):
        #visiting
        #left
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        #right
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                return other
    def parenthesize(self,T,p):
        print(p.element, end = '')
        if not T.is_leaf(p):
            first_time = True
            for c in T.children(p):
                sep = '(' if first_time else ','
                print(sep, end = '')
                first_time = False
                self.parenthesize(T,c)
            print(')', end = '')
    
    def index(self,element,arr,list_ = []):
        val = None
        for x,y in enumerate(arr):
            if isinstance(y,list):
                list_ = self.index(element,arr[x],list_ + [x])
                if element not in [n for n in self.flatten(arr[x])]: 
                    list_.pop()
            if y == element:
                val = [x]
        return list_ + val if val else list_ 

    def flatten(self,something):
        if isinstance(something, (list, tuple, set, range)):
            for sub in something:
                yield from self.flatten(sub)
        else:
            yield something


    def inserter(self,list_,seq,value):
        val = []
        for x,y in enumerate(seq[:-1]):
            val = list_[y] if x == 0 else val[y]
        val.append(value)

    def __str__(self):
        temp = []
        if not self.is_empty():
            Q = Queue()
            Q.enqueue(self.root())
            temp.append([self.root().element])
            while not Q.is_empty():
                p = Q.dequeue()
                for c in self.children(p):
                    Q.enqueue(c)
                    index = self.index(p.element,temp)
                    self.inserter(temp,index,[c.element])
        return str(temp)

if __name__ == '__main__':
    ting = LinkedBinaryTree()
    ting._add_root('Francis of the Filth')
    right = ting._add_right(ting.root(),'Pink guy')
    left =  ting._add_left(ting.root(),'chin chin')
    ting._add_left(left, 'salamander_man')
    ting._add_right(left, 'Safari man')
    ting._add_right(right, 'eye of the Dubz')
    ting._add_left(right, 'Edward watermelon hands')
    
    ting2 = LinkedBinaryTree()
    ting2._add_root('Joji')
    ting2._add_left(ting2.root(),'Rich Chigga')
    ting2._add_right(ting2.root(),'Sad Boy UwU')

    ting3 = LinkedBinaryTree()
    ting3._add_root('George Miller')
    ting3._attach(ting3.root(),ting,ting2)

    ting3.display()
    print(ting3)