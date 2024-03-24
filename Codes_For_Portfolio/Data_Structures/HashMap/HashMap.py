class HashMap:
    def __init__(self):
        self.size = 100
        self.map = [None] * self.size
        self.count = 0

    def _get_hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def add(self, key, value):
        if self.count >= self.size * 0.7:
            self.resize()
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            self.count += 1
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            self.count += 1

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for i, pair in enumerate(self.map[key_hash]):
                if pair[0] == key:
                    self.map[key_hash].pop(i)
                    self.count -= 1
                    return True
        return False

    def print(self):
        for item in self.map:
            if item is not None:
                for pair in item:
                    print(str(pair))

    def resize(self):
        old_map = self.map
        self.size *= 2
        self.map = [None] * self.size
        self.count = 0
        for index in old_map:
            if index is not None:
                for pair in index:
                    self.add(pair[0], pair[1])



        
        
        


    
        

