from _template import SortTemplate
import unittest
import random


class SelectionSort(SortTemplate):

    def sort(self):
        for i in range(len(self.arr)):
            min = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] <= self.arr[min]:
                    min = j
            self.exch(i, min)


class SelectionSortTests(unittest.TestCase):

    def test_basic(self):
        example = SelectionSort([5, 4, 3, 2, 1])
        example.sort()
        self.assertEqual(example.isSorted(), True)

    def test_one_elem(self):
        example = SelectionSort([1])
        example.sort()
        self.assertEqual(example.isSorted(), True)

    def test_random_thousand_elements(self):
        lst = [random.randint(0, 1000) for x in range(1000)]
        example = SelectionSort(lst)
        example.sort()
        self.assertEqual(example.isSorted(), True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SelectionSortTests))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
