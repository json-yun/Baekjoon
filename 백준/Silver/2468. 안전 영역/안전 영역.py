import sys

N = int(sys.stdin.readline())
A = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

def main() -> None:
    # 수위(level)을 입력받아 수위 이하인 경우 0으로 표시해 리턴
    def _flood(level :int) -> list:
        is_dry = [[e if e > level else 0 for e in row] for row in A]
        return is_dry
    
    def _check_neighbor(is_dry :list, neighbor_list :list, merged_islands_list :list, row_idx :int, col_idx :int) -> int:
        r_neighbor = c_neighbor = -1
        if row_idx > 0 and is_dry[row_idx-1][col_idx]>=1:
            r_neighbor = neighbor_list[row_idx-1][col_idx]
        if col_idx > 0 and is_dry[row_idx][col_idx-1]>=1:
            c_neighbor = neighbor_list[row_idx][col_idx-1]
        if r_neighbor == -1:
            return c_neighbor
        elif c_neighbor == -1:
            return r_neighbor
        elif r_neighbor == c_neighbor:
            return r_neighbor
        else:
            merge_island = (min(r_neighbor, c_neighbor), max(r_neighbor, c_neighbor))
            if merge_island not in merged_islands_list:
                merged_islands_list.append(merge_island)
            return merge_island[0]
        
    # def _make_island(is_dry :list):
    #     merged_islands_list = []
    #     new_island = 1
    #     neighbor_list = [[] for _ in range(N)]
    #     for i, row in enumerate(A):
    #         for j, e in enumerate(row):
    #             if is_dry[i][j] == 0:
    #                 neighbor_list[i].append(-1)
    #                 continue
    #             island_num = _check_neighbor(is_dry, neighbor_list, merged_islands_list, i, j)
    #             # 섬 번호가
    #             if island_num == -1:
    #                 neighbor_list[i].append(new_island)
    #                 new_island += 1
    #             else:
    #                 neighbor_list[i].append(island_num)
        
    #     for i in neighbor_list:
    #         print(["○" if a==-1 else "●" for a in i])
    #     return new_island-len(merged_islands_list)-1
    
    
    def _make_island(is_dry: list) -> int:
        def find_root(island_map, island):
            while island_map[island] != island:
                island_map[island] = island_map[island_map[island]]  # 경로 압축
                island = island_map[island]
            return island
        
        def union_islands(island_map, island1, island2):
            root1 = find_root(island_map, island1)
            root2 = find_root(island_map, island2)
            if root1 != root2:
                island_map[root2] = root1  # 병합

        merged_islands_list = []
        new_island = 1
        N = len(is_dry)
        M = len(is_dry[0])
        neighbor_list = [[] for _ in range(N)]
        island_map = {}  # 각 섬 번호의 루트를 기록

        for i in range(N):
            for j in range(M):
                if is_dry[i][j] == 0:
                    neighbor_list[i].append(-1)
                    continue
                island_num = _check_neighbor(is_dry, neighbor_list, merged_islands_list, i, j)
                if island_num == -1:
                    neighbor_list[i].append(new_island)
                    island_map[new_island] = new_island
                    new_island += 1
                else:
                    neighbor_list[i].append(island_num)
                    if island_num not in island_map:
                        island_map[island_num] = island_num

        # 병합 처리
        for island1, island2 in merged_islands_list:
            union_islands(island_map, island1, island2)

        # 고유 섬의 루트 번호 개수 세기
        unique_islands = set(find_root(island_map, island) for island in island_map.keys())


        return len(unique_islands)

    
    
    unique_heights = []
    for row in A:
        for e in row:
            if e not in unique_heights:
                unique_heights.append(e)
    
    max_island = 1
    unique_heights.sort()
    unique_heights.pop(-1)
    for i in unique_heights:
        is_dry = _flood(i)
        islands = _make_island(is_dry)
        max_island = max(max_island, islands)
    print(max_island)

main()