from _template import SortTemplate


class InsertionSort(SortTemplate):

    def sort(self):
        for i in range(1, len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j-1]:
                    self.exch(j, j - 1)
                else:
                    break
