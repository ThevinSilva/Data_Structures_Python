from linked_binary_tree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    '''

        :token: - as an isolated leaf should be one singular number
                - in a three part subtree it's the operator


    '''

    
    def __init__(self,token,left = None,right = None):
        super().__init__()
        if not isinstance(token,str):
            raise ValueError('Token should be string')
        self._add_root(token)
        if left is not None:
            if token not in '+-x/':
                raise ValueError('Token must be a valid operator')
            self._attach(self.root(),left,right)

        
    def __str__(self):
        pieces = []
        self._parenthsize_recur(self.root(),pieces)
        return ''.join(pieces)

    def _parenthsize_recur(self,p,result):
        if self.is_leaf(p):
            result.append(str(p.element))
        else:
            result.append('(')
            self._parenthsize_recur(self.left(p),result)
            result.append(p.element)
            self._parenthsize_recur(self.right(p),result)
            result.append(')')

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self,p):
        if self.is_leaf(p):
            return p.element
        else:
            op = p.element
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+': return left_val + right_val
            if op == '-': return left_val - right_val
            if op == '/': return left_val / right_val
            if op == 'x': return left_val * right_val

def build_expression_tree(tokens):
    S = []
    for t in tokens:
        if t in '+-x/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op,left,right))
    return S.pop()