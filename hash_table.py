import math

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for buckets in range(size)]

    def save(self, key, value):
        hash_code = self.hash_func(key)
        self.hash_table[hash_code].append((key, value, []))

    def load(self, key):
        hash_code = self.hash_func(key)
        for node in self.hash_table[hash_code]:
            if (node[0] == key):
                return node

    def addLink(self, key_1, key_2):
        hash_code_1 = self.hash_func(key_1)
        hash_code_2 = self.hash_func(key_2)

        # Add link to first node
        for node in self.hash_table[hash_code_1]:
            if(node[0] == key_1):
                node[2].append(key_2)

        # Add link to second node
        for node in self.hash_table[hash_code_2]:
            if(node[0] == key_2):
                node[2].append(key_1)

    def hash_func(self, key):
        uni_sum = sum([ord(char) for char in key])
        size = len(key)

        return int(math.floor(uni_sum / size) % self.size)


if __name__ == '__main__':
    table = HashTable(4)

    table.save('qwerty', 1)
    table.save('uiop', 4)
    table.save('asdf', -2)
    table.save('monkey', 666)
    table.save('boink', 77)

    table.addLink('qwerty', 'monkey')

    print(table.load('qwerty'))
    print(table.load('uiop'))
    print(table.load('asdf'))
    print(table.load('monkey'))
    print(table.load('boink'))
