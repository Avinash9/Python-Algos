
class BinaryMinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,number):
        self.heapList.append(number)
        self.currentSize = self.currentSize + 1
        self.preup(self.currentSize)

    def preup(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i //= 2