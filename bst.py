import random

class Node():
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree():
    def __init__(self, root_node):
        self.root = root_node

    def insert(self, in_data):
        current = self.root
        newNode = Node(in_data)

        while(1):
            # New data is duplicate
            if(in_data == current.data):
                newNode.lchild = current.lchild
                current.lchild = newNode
                return
            # New data is less than
            if (in_data < current.data):
                #Empty spot found
                if(current.lchild == None):
                    current.lchild = newNode
                    return
                else:
                    current = current.lchild
            # New data is greater than
            else:
                if(current.rchild == None):
                    current.rchild = newNode
                    return
                else:
                    current = current.rchild


    def retrieve(self, data):
        current = self.root
        while(1):
            if current is None:

                return None

            if (current.data == data):
                return current

            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild

    def update(self, target_data, new_data):
        target = retrieve(target_data)
        target.data = new_data

if __name__ == '__main__':
    root = Node(5)
    tree = Tree(root)

    for i in range(3):
        new = random.randint(-10, 10)
