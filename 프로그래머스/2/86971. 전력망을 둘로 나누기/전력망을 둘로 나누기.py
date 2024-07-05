# 3.66ms 
def solution(n, wires):
    # find leaf nodes
    # get lowest weight between leaf nodes
    # add
    
    # [weight, is_not_leaf, parent]
    nodes = {i+1: [1, -1, 0] for i in range(n)}
    min_weight_a, min_weight_b = 1, 2
    while len(nodes) > 2:
        for wire in wires:
            if wire[0] in nodes:
                nodes[wire[0]][1] += 1
                nodes[wire[0]][2] = wire[1]
            if wire[1] in nodes:
                nodes[wire[1]][1] += 1
                nodes[wire[1]][2] = wire[0]
        nodes_ = list(nodes.items())

        min_weight_a = min_weight_b = 101
        for node in nodes.items():
            weight, is_not_leaf, parent = node[1]
            if not is_not_leaf:
                min_weight_a = min(min_weight_a, weight)
                min_weight_b = min(min_weight_b, weight+nodes[parent][0])
        
        for node in nodes_:
            weight, is_not_leaf, parent = node[1]
            if not is_not_leaf and (weight == min_weight_a or weight+nodes[parent][0] == min_weight_b):
                nodes[parent][0] += weight
                if [node[0], parent] in wires:
                    wires.pop(wires.index([node[0], parent]))
                else:
                    wires.pop(wires.index([parent, node[0]]))
                del nodes[node[0]]
            node[1][1] = -1
        print(wires, nodes, min_weight_a, min_weight_b)
        if len(nodes) == 1:
            return list(nodes.values())[0][0] - min_weight_a * 2
        
    last = list(nodes.values())
    answer = abs(last[0][0] - last[1][0])
    return answer 