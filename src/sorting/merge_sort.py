from _template import SortTemplate


class MergeSort(SortTemplate):

    def merge(self, lo, mid, hi):
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            self.aux[k] = self.arr[k]
        for k in range(lo, hi + 1):
            if i > mid:
                self.arr[k] = self.aux[j]
                j += 1
            elif j > hi:
                self.arr[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                self.arr[k] = self.aux[j]
                j += 1
            else:
                self.arr[k] = self.aux[i]
                i += 1


class DescendingMergeSort(MergeSort):

    def sort(self):
        self.aux = [0] * len(self.arr)
        self.sub_sort(0, len(self.arr) - 1)

    def sub_sort(self, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        self.sub_sort(lo, mid)
        self.sub_sort(mid + 1, hi)
        self.merge(lo, mid, hi)


class AscendingMergeSort(MergeSort):

    def sort(self):
        self.aux = [0] * len(self.arr)
        sz = 1
        while sz < len(self.arr):
            lo = 0
            while lo < len(self.arr) - sz:
                self.merge(lo, lo + sz - 1, min(lo + sz + sz - 1, len(self.arr) - 1))
                lo += sz + sz
            sz += sz
