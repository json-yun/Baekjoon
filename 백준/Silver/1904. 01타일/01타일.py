import sys

input = sys.stdin.readline

def main() -> None:
    def tiles(n: int) -> int:
        r = [1, 1]
        
        for i in range(n-1):
            a, b = (i+1)%2, i%2
            
            if (r[a], r[b]) not in cache:
                cache[(r[a], r[b])] = sum(r)%15746
            r[b] = cache[(r[a], r[b])]
            
        return r[n%2]
    
    cache = {}
    print(tiles(int(input())))

if __name__ == "__main__":
    main()