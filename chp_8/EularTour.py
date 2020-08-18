class EularTour:
    def __init__(self,tree):
        self._tree = tree
    
    @property
    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(),0,[])
    
    def _tour(self,p,d,path):
        '''
        Perform tour of subtree rooted at Position p.
        p Position of current node being visited
        d depth of p in the tree
        path list of indices of children on path from root to p
        '''
        result = []
        self._hook_previsit(p,d,path)
        for c in self._tree.children(p):
            result.append(self._tour(c,d + 1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p,d,path,result)
        return answer

    def _hook_postvisit(self,p,d,path,result):
        pass

    def _hook_previsit(self,p,d,path):
        pass
