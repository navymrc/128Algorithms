class OurQueue:
    def __int__(self, items):
        self.heap = []
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap)

    def push(self, x):
        assert x not in self.rank
        i = len(self)
        self.heap.append(x)
        self.rank[x] = i
        self.up(i)

    def pop(self):
        assert len(self.heap) is not 0
        root = self.heap[0]
        del self.rank[root]
        x = self.heap.pop()
        if self:
            self.heap[0] = x
            self.rank[x] = 0
            self.down(0)
        return root

    def up(self, i):
        x = self.heap[i]
        p_i = self.parent(i)
        while 0 < i < self.heap[p_i]:
            p = self.heap[p_i]
            self.heap[i] = self.heap[p_i]
            self.heap[p_i] = self.heap[x]


        pass

    def parent(self, i):
        """Binary three"""
        return (i-1) // 2

    def children(self, i):
        """Binary three"""
        return [(2*i)+1, 2*(i+1)]

    def dow(self, i):
        pass

