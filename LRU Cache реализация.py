class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.d = dict()
        self.head, self.tail = Node(0, 0), Node(0, 0)  # фейк узлы
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):  # вырезать
        node.prev.next, node.next.prev = node.next, node.prev

    def _add(self, node):  # вставить вперёд
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1  # нет такого

    def put(self, key, val):
        if key in self.d:
            self._remove(self.d[key])
        node = Node(key, val)
        self._add(node)
        self.d[key] = node
        if len(self.d) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.d[lru.key]  # выкинули старый