from _template import SortTemplate


class SelectionSort(SortTemplate):

    def sort(self):
        for i in range(len(self.arr)):
            min = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] <= self.arr[min]:
                    min = j
            self.exch(i, min)
