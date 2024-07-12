from typing import Iterable
from queue import Queue
import sys
input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.neighbors: list[int] = []
        self.neighbors.sort()
    
    def add_neighbor(self, *keys) -> None:
        for key in keys:
            self.neighbors.append(key)
        self.neighbors.sort()

class Graph:
    def __init__(self, size: int) -> None:
        self.parents = {i: i for i in range(1, size+1)}
    
    def find_parent(self, key) -> int:
        while self.parents[key] != key:
            key = self.parents[key]
        return key
    
    def insert(self, vertex: Vertex) -> None:
        vertex.neighbors.sort()
        for neighbor in vertex.neighbors:
            parents_me = self.find_parent(vertex.key)
            parents_neighbor = self.find_parent(neighbor)
            self.parents[parents_neighbor] = parents_me
            self.parents[vertex.key] = parents_me

def main() -> None:
    N = int(input())
    M = int(input())
    vs: dict[Vertex] = {i: Vertex(i) for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        vs[a].add_neighbor(b)
        vs[b].add_neighbor(a)
    
    visited = [0 for _ in range(N+1)]
    q = Queue()
    q.put(vs[1])
    while not q.empty():
        now = q.get()
        visited[now.key] = 1
        for n in now.neighbors:
            q.put(vs[n]) if visited[n]==0 else None
        
    print(sum(visited)-1)

main()