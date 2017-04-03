from _template import SortTemplate
import random


class QSort(SortTemplate):

    def sort(self):
        random.shuffle(self.arr)
        self.arr = QSort.sub_sort(self.arr)

    @staticmethod
    def sub_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left, right = [], []
            for x in arr[1:]:
                if x < pivot:
                    left.append(x)
                else:
                    right.append(x)
            return QSort.sub_sort(left) + [pivot] + QSort.sub_sort(right)
