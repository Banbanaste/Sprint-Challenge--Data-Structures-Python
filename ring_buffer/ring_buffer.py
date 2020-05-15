class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.oldestinlist = None

    def append(self, item):

        if not len(self.list):
            self.oldestinlist = item

        if self.capacity is len(self.list):
            self.list = [
                x if x is not self.oldestinlist else item for x in self.list]

            if len(self.list) == (self.list.index(item) + 1):
                self.oldestinlist = self.list[0]
            else:
                self.oldestinlist = self.list[self.list.index(item) + 1]

        else:
            self.list.append(item)

    def get(self):
        return self.list
