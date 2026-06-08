class Heap:
    def __init__(self, max_heap=True): # false가 들어오면 min으로
        self.heap = []
        self.compare = (lambda a, b: a > b) if max_heap else (lambda a, b: a < b)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def print_heap(self):
        kind = "MaxHeap" if self.compare(1, 0) else "MinHeap"
        print(f"{kind}: {self.heap}")

    def heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.compare(self.heap[idx], self.heap[parent]):
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self.heapify_up(parent)

    def heapify_down(self, idx):
        target = idx
        left, right = 2 * idx + 1, 2 * idx + 2

        if left  < len(self.heap) and self.compare(self.heap[left],  self.heap[target]):
            target = left

        if right < len(self.heap) and self.compare(self.heap[right], self.heap[target]):
            target = right

        if target != idx:
            self.heap[idx], self.heap[target] = self.heap[target], self.heap[idx]
            self.heapify_down(target)




max_heap = Heap(max_heap=True)

for v in [5, 3, 8, 1, 9]:
    max_heap.insert(v)

max_heap.print_heap()       # MaxHeap: [9, 8, 5, 1, 3]
print(max_heap.delete())    # 9

min_heap = Heap(max_heap=False)

for v in [5, 3, 8, 1, 9]:
    min_heap.insert(v)
min_heap.print_heap()       # MinHeap: [1, 3, 8, 5, 9]
print(min_heap.delete())    # 1