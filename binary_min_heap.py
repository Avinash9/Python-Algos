
class BinaryMinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,number):
        self.heapList.append(number)
        self.currentSize = self.currentSize + 1
        self._preup(self.currentSize)

    def _preup(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i //= 2

    def delete(self):
        del_val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self._precdown(1)
        return del_val

    def _precdown(self,index):
        while index*2 <= self.currentSize :
            new_index = self._check_min_child(index)
            if self.heapList[index] > self.heapList[new_index]:
                temp = self.heapList[index]
                self.heapList[index] =  self.heapList[new_index]
                self.heapList[new_index] = temp
            index = new_index


    def _check_min_child(self,index):
        if self.currentSize < 2*index + 1:
            return 2*index
        else:
            if self.heapList[2*index] >  self.heapList[2*index+1]:
                return 2*index +1
            else:
                return 2*index





