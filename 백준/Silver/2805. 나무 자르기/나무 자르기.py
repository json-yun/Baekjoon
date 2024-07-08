import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
TREE = [int(i) for i in sys.stdin.readline().split()]
TREE.sort()
TREE_REV = TREE[::-1]

def main():
    def _cut_tree(height :int, from_top :bool) -> int:
        result = 0
        for i in TREE_REV if from_top else TREE:
            if i > height:
                result += i-height
            elif i <= height:
                if from_top:
                    break
                else:
                    continue
        return result
    
    def _bin_search(target :int, start :int, end :int):
        nonlocal max_height
        if end < start:
            return
        else:
            middle = (start + end)//2
            result_mid = _cut_tree(middle, middle>N//2)
            if result_mid == target:
                max_height = max(max_height, middle)
            elif target < result_mid:
                max_height = max(max_height, middle)
                _bin_search(target, middle+1, end)
            else:
                _bin_search(target, start, middle-1)
        
    max_height = 0
    _bin_search(M, 0, TREE[-1])
    print(max_height)

main()