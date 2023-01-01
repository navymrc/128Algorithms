class OurHeap:
    """Binary Heap Priority"""

    def __init__(self, heap=[]):
        self.heap = heap

    def __len__(self):
        return len(self.heap)

    @staticmethod
    def __children(current_index: int) -> list[int]:
        return [(2 * current_index) + 1, 2 * (current_index + 1)]

    @staticmethod
    def __parent(current_index: int) -> int:
        return (current_index - 1) // 2

    def __down(self, index):
        a, b = self.__children(index)
        if a >= len(self.heap) or b >= len(self.heap):
            return False

        while True:
            if self.heap[index] > a and self.heap[a] < self.heap[b]:
                self.__swap(index, a)
                self.__down(a)
                break
            elif self.heap[index] > b and self.heap[b] < self.heap[a]:
                self.__swap(index, b)
                self.__down(b)
                break
            else:
                break

    def __swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        return self.heap

    def __up(self, index):
        parent = self.__parent(index)
        if parent < 0:
            return False

        while True:
            if self.heap[index] < self.heap[parent]:
                self.__swap(index, parent)
                self.__up(parent)
                break
            else:
                break

    @property
    def value(self):
        return self.heap

    def pop(self):
        def init():
            self.__swap(0, len(self.heap)-1)
            z = self.heap.pop()
            return z

        x = init() if len(self.heap) != 0 else None
        self.__down(0)
        return x

    def push(self, item):
        self.heap.append(item)
        self.__up(len(self.heap) - 1)

    def update(self, index, item):
        """"""
        if index < len(self.heap):
            self.heap[index] = item
            self.__up(index) if self.__parent(index) > item else self.__down(index)
        else:
            return None


A = OurHeap([2, 5, 7, 13, 9, 8, 30, 20, 17, 11, 12, 15])
print(f"{A.value}\n{A.pop()}\n{A.value}")
A.update(3, 0)
A.push(6)
print(f"{A.pop()}\n{A.value}")
