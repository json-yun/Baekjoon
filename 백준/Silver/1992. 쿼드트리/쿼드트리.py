import sys

N = int(sys.stdin.readline())
A = [[int(i) for i in list(sys.stdin.readline().strip())] for _ in range(N)]

# 왼쪽 위 좌표와 너비(높이)를 입력받아 배열의 합을 반환
def sum_array(row: int, col: int, width: int) -> int:
    result = 0
    for i in A[row:row+width]:
        result += sum(i[col:col+width])
    return result

def quad_tree(row: int, col: int, width: int) -> str:
    if (s:=sum_array(row, col, width)) in (0, width**2):
        return str(s//(width**2))
    else:
        width_h = width//2
        results = ""
        results += "("
        results += quad_tree(row, col, width_h)
        results += quad_tree(row, col+width_h, width_h)
        results += quad_tree(row+width_h, col, width_h)
        results += quad_tree(row+width_h, col+width_h, width_h)
        results += ")"
        return results
    
print(quad_tree(0, 0, N))