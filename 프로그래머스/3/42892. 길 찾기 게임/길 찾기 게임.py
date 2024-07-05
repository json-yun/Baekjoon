import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, n: int, left: ("Node", None)=None, right: ("Node", None)=None):
        self.n = n
        self.left = left
        self.right = right
    
    def order(self):
        def _order(node: ("Node", None)) -> None:
            if node is None:
                return
            res[0].append(node.n)
            _order(node.left)
            _order(node.right)
            res[1].append(node.n)
            return
        res = [[], []]
        _order(self)
        return res

def solution(nodeinfo):
    answer = [[]]
    nodes_x = sorted([[v[0], [v[1], i+1]] for i, v in enumerate(nodeinfo)])
    nodes_y = {}
    for x, _ in nodes_x:
        y, i = _
        try:
            nodes_y[y].append([x, i])
        except (AttributeError, KeyError):
            nodes_y[y] = [[x, i]]
    def makenode(parent: ("Node", None), descendants: dict,
                 left_limit: int, right_limit: int) -> "Node":
        descendants = descendants.copy()
        childs = descendants.pop(max(descendants))
        node = None
        for child in childs:
            if child[0] < left_limit:
                continue
            elif child[0] > right_limit:
                return None
            else:
                node = Node(child[1])
                break
        if node and descendants:
            node.left = makenode(node, descendants, left_limit, child[0])
            node.right = makenode(node, descendants, child[0], right_limit)
        return node
            
    root = makenode(None, nodes_y, -1, 100001)
    answer = root.order()
    return answer