class OurHeap:
    """
    Binary Heap Priority
    The structure contains an array heap.
    The principal operations are push and pop. A new element is inserted with push.
    The minimal element is extracted with pop.
    The average complexity of the operations on our heap is O(logn); however, the worst-case complexity is O(n).
    """

    def __init__(self, heap=[]):
        """
        Default will be represented as a list.
        Or you can also insert your heap in as a list
        :param: heap: list[int]
        :return: void
        """
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
        """
        The action of down consists of an exchange between a node and its child with the smallest value.
        :param index: int
        :return: boolean or None
        """
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
        """
        Up effects a series of exchanges of a node with its parents,
        climbing up the tree until the heap order is respected.
        :param index: int
        :return: boolean or None
        """
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
        """
        Return the heap as a list.
        :return: list[int]
        """
        return self.heap

    def pop(self):
        """
        The minimal element is extracted with pop: the root is replaced by the last leaf in the heap,
        and then the heap is reorganised to respect the heap order.
        :return: int or None
        """
        def init():
            self.__swap(0, len(self.heap)-1)
            z = self.heap.pop()
            return z

        x = init() if len(self.heap) != 0 else None
        self.__down(0)
        return x

    def push(self, item):
        """
        A new element is added as the last leaf in the heap,
        and then the heap is reorganised to respect the heap order.
        :param item: int
        :return: void
        """
        self.heap.append(item)
        self.__up(len(self.heap) - 1)

    def update(self, index, item):
        """
        The method update permits the value of a heap element to be changed.
        It then calls up or down to preserve the heap order.
        :param index: int
        :param item: int or float
        :rtype: None
        :return: void or None
        """
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
