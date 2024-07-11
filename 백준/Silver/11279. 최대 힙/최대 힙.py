import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for i in range(N)]

class MaxHeap:
    def __init__(self) -> None:
        self._data = []
    def __len__(self) -> int:
        return len(self._data)
    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]
    def _maxheap_down(self, parent) -> None:
        length = len(self)
        while True:
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2
            largest = parent
            
            if left_child < length and self._data[left_child] > self._data[largest]:
                largest = left_child
                
            if right_child < length and self._data[right_child] > self._data[largest]:
                largest = right_child
                
            if largest == parent:
                break
            
            self._swap(parent, largest)
            parent = largest
    def _maxheap_up(self, child) -> None:
        while child > 0:
            parent = (child - 1) // 2
            if self._data[child] > self._data[parent]:
                self._swap(child, parent)
                child = parent
            else:
                break
    def pop_root(self) -> int:
        if (l := len(self)) <= 0:
            return 0
        else:
            self._swap(0, l-1)
            root = self._data.pop()
            self._maxheap_down(0)
            return root
    def insert(self, value: int) -> None:
        self._data.append(value)
        self._maxheap_up(len(self)-1)

def main() -> None:
    heap = MaxHeap()
    for i in A:
        if i == 0:
            print(heap.pop_root())
        else:
            heap.insert(i)
    print()

main()