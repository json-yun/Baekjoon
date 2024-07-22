import sys

input = sys.stdin.readline

def main() -> None:
    def tiles(n_left: int) -> int:
        result = [1, 1]
        for i in range(n_left-1):
            if (result[(i+1)%2], result[i%2]) not in cache:
                cache[(result[(i+1)%2], result[i%2])] = sum(result)%15746
            result[i%2] = cache[(result[(i+1)%2], result[i%2])]
        return result[n_left%2]
    cache = {}
    print(tiles(int(input())))

if __name__ == "__main__":
    main()