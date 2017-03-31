from _template import SortTemplate


class ShellSort(SortTemplate):

    def sort(self):
        h = 1
        while h < len(self.arr) // 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, len(self.arr)):
                for j in range(i, h-1, -h):
                    if self.arr[j] <= self.arr[j - h]:
                        self.exch(j, j - h)
                    else:
                        break
            h = h // 3
