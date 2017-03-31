from _template import SortTemplate
import unittest
import random


class InsertionSort(SortTemplate):

    def sort(self):
        for i in range(1, len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j-1]:
                    self.exch(j, j - 1)
                else:
                    break


class InsertionSortTests(unittest.TestCase):

    def test_basic(self):
        example = InsertionSort([5, 4, 3, 2, 1])
        example.sort()
        self.assertEqual(example.isSorted(), True)

    def test_one_elem(self):
        example = InsertionSort([1])
        example.sort()
        self.assertEqual(example.isSorted(), True)

    def test_random_thousand_elements(self):
        lst = [random.randint(0, 1000) for x in range(1000)]
        example = InsertionSort(lst)
        example.sort()
        self.assertEqual(example.isSorted(), True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(InsertionSortTests))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())