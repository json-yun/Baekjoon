import sys

N, B = [int(i) for i in sys.stdin.readline().split()]
MATRIX = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
for i in range(N):
    MATRIX[i] = tuple(map(lambda x: x%1000, MATRIX[i]))
MATRIX = tuple(MATRIX)

def main() -> None:
    transpose_cache = {}
    def transpose(matrix: list) -> list:
        if matrix in transpose_cache:
            return transpose_cache[matrix]
        else:
            n = len(matrix)
            result = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(matrix[j][i])
                result.append(tuple(row))
            result = tuple(result)
            transpose_cache[matrix] = result
            return result

    product_cache = {}
    def matrix_product(matrix_0: list, matrix_1: list=None) -> list:
        if matrix_1 is None:
            matrix_1 = matrix_0
        if (matrix_0, matrix_1) in product_cache:
            return product_cache[(matrix_0, matrix_1)]
        else:
            n = len(matrix_0)
            matrix_T = transpose(matrix_1)
            result = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(sum(x*y for x, y in zip(matrix_0[i], matrix_T[j]))%1000)
                result.append(tuple(row))
            result = tuple(result)
            product_cache[(matrix_0, matrix_1)] = result
            return result
        
    cache = {}
    def devide_conquer(matrix: list, B: int) -> int:
        B_half = B//2
        if B==1:
            return matrix
        elif B==2:
            return matrix_product(matrix)
        if B_half > 1:
            if (matrix, B_half) in cache:
                left = cache[(matrix, B_half)]
            else:
                left = devide_conquer(matrix, B_half)
        else:
            left = matrix
        if B == B_half:
            right = left
        elif B-B_half > 1:
            if (matrix, B-B_half) in cache:
                right = cache[(matrix, B-B_half)]
            else:
                right = devide_conquer(matrix, B-B_half)
        else:
            right = matrix
        result = matrix_product(left, right)
        if (matrix, B) not in cache:
            cache[(matrix, B)] = result
        return result
    
    answer = devide_conquer(MATRIX, B)
    for i in range(N):
        print(" ".join(map(str, answer[i])))

main()