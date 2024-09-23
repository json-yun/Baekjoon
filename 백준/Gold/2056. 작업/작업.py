import sys
from queue import PriorityQueue
input = sys.stdin.readline

def main() -> None:
    def find_next_task() -> int:
        for i in TASKS:
            if scheduled[i]:
                continue
            if TASKS[i][0] == 0:
                return i

        return 0

    def schedule(task: int) -> None:
        time_table.put((clock+TASKS[p][1], p)) # (end_time, task)
        scheduled[p] = True
    
    N = int(input())
    TASKS: dict[int, list] = {}
    postwork = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        burst, n_prior, *P = map(int, input().split())
        TASKS[i] = [n_prior, burst, P]
        for p in P:
            postwork[p].append(i)
    scheduled = [False for _ in range(N+1)]

    clock = 0
    time_table = PriorityQueue()
    while p:=find_next_task():
        schedule(p)
    while TASKS:
        clock, task_end = time_table.get()
        TASKS.pop(task_end)
        for p in postwork[task_end]:
            TASKS[p][0] -= 1
            if TASKS[p][0] == 0:
                schedule(p)
                    

    print(clock)

if __name__ == "__main__":
    sys.exit(main())