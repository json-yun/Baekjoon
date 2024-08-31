def main():
    def find_quadrant(r: int, c: int, level: int) -> tuple[int]:
        border = 2**(level-1)
        q = 0
        
        if r >= border:
            q += 2
            r -= border
        if c >= border:
            q += 1
            c -= border

        return (q, r, c)
    
    N, r, c = map(int, input().split())
    
    result = 0
    for level in range(N, 0, -1):
        q, r, c = find_quadrant(r, c, level)
        result += q * (4**(level-1))
        
    print(result)

if __name__ == "__main__":
    main()