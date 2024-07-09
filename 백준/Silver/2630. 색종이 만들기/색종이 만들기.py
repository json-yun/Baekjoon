import sys

N :int = int(sys.stdin.readline())
PAPER :list = [[int(a) for a in sys.stdin.readline().split()] for _ in range(N)]

def main() -> None:
    # 색종이가 한가지 색으로 이루어졌으면 색깔(0또는1)을, 아니면 -1을 반환
    def _check_papers(row :int, col :int, width :int) -> int:
        total_std = sum(PAPER[row][col:col+width])
        if total_std != width and total_std!=0:
            return -1
        for i in PAPER[row+1:row+width]:
            total = sum(i[col:col+width])
            if total!=total_std:
                return -1
        return total_std//width
    
    # 색종이를 4등분해 시작 인덱스를 반환
    def _cut_papers(row :int, col :int, width :int) -> list[tuple]:
        new_width :int = width//2
        return [(row, col), (row+new_width, col), (row, col+new_width), (row+new_width, col+new_width)]
    
    # 한 가지 색으로 구성된 색종이라면 n_papers에 색깔 별 개수를 추가
    # 아니라면 4등분 하고 다시 색종이별로 판별
    def _make_papers(row :int, col :int, width :int) -> None:
        paper = _check_papers(row, col, width)
        if paper != -1:
            n_papers[paper] += 1
        else:
            for i, j in _cut_papers(row, col, width):
                _make_papers(i, j, width//2)
                    
    n_papers = [0, 0]
    _make_papers(0, 0, N)
    print(n_papers[0])
    print(n_papers[1])
    
main()