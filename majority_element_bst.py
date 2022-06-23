class Node:
    def __int__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1

    def add_child(self, data):
        if data == self.data:
            self.