class NodeHeap:
    def __init__(self, key, value):
        self.priority = key
        self.value = value
        self.degree = 0  # колво детей узлов
        self.parent = None
        self.child = None  # left
        self.sibling = None  # right


class Heap:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, key, value):
        new_heap = Heap()
        new_node = NodeHeap(key, value)
        new_heap.head = new_node
        self.merge(new_heap)

        return new_node

    def get_minimum(self):
        if not self.head:
            return None
        min_node = self.head
        cur = self.head.sibling
        while cur:
            if cur.key < min_node.key:
                min_node = cur
            cur = cur.sibling

        return min_node.key

    def merge(self, other_head):
        if not self:
            return other_head
        if not other_head:
            return self
        result = None
        curr = None
        p1 = self
        p2 = other_head
        if p1.degree <= p2.degree:
            result = p1
            p1 = p1.sibling
        else:
            result = p2
            p2 = p2.sibling
        curr = result
        while p1 and p2:
            if p1.degree <= p2.degree:
                curr.sibling = p1
                p1 = p1.sibling
            else:
                curr.sibling = p2
                p2 = p2.sibling
            curr = curr.sibling
        if p1:
            curr.sibling = p1
        else:
            curr.sibling = p2

        return result
