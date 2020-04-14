class LRU:
    def init (self, size):
        self.size = size
        cache = {}
        lru = []