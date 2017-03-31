import unittest
import random
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from shellsort import ShellSort


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
    suite.addTest(unittest.makeSuite(ShellSortTests))
    suite.addTest(unittest.makeSuite(SelectionSortTests))
    suite.addTest(unittest.makeSuite(InsertionSortTests))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
