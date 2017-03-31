from _template import SortTemplate
import unittest
import random


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


class ShellSortTests(unittest.TestCase):

    def test_basic(self):
        example = ShellSort([5, 4, 3, 2, 1])
        example.sort()
        self.assertEqual(example.isSorted(), True)

    def test_one_elem(self):
        example = ShellSort([1])
        example.sort()
        self.assertEqual(example.isSorted(), True)

    def test_random_thousand_elements(self):
        lst = [random.randint(0, 1000) for x in range(1000)]
        example = ShellSort(lst)
        example.sort()
        self.assertEqual(example.isSorted(), True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ShellSortTests))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
