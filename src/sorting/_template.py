class SortTemplate:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        raise NotImplementedError

    def exch(self, i, j):
        t = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = t

    def show(self):
        print(self.arr)

    def isSorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i - 1]:
                return False
        return True
