class HashTable:
    def __init__(self):
        self.size = 128
        self.hash_table = [[] for _ in range(self.size)]

    def _hash(self, value):
        summ = 0
        for symbol in value:
            summ += ord(symbol)
        return summ % self.size

    def put(self, key, value):
        index = self._hash(key)
        table = self.hash_table[index]
        if key not in table:
            self.hash_table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        table = self.hash_table[index]
        for i, (k, v) in enumerate(table):
            if key == k:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        table = self.hash_table[index]
        for i, (k, v) in enumerate(table):
            if key == k:
                self.hash_table[index].pop(i)
                break
        return
