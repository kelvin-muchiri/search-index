"""Search a value in a collection and return index of first occurrence."""

import unittest

ORIGINAL_INDICES = {}

def get_list_original_indices(alist):
    """Store the original array indices."""
    for i in range(len(alist)):
        # Only store the index of the first occurrence
        if not alist[i] in ORIGINAL_INDICES:
            ORIGINAL_INDICES[alist[i]] = i


def merge_sort(alist):
    """Sort list in ascending order."""

    # The base case: If the list is empty or
    # has one item
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        # Invoking the recursive calls
        # below assume that the left and right halves are
        # sorted
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # place the items back in the original
        # list by taking the smallest item from the sorted
        # lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1

            else:
                alist[k] = right[j]
                j = j + 1

            k = k + 1

        # Check if any element was left
        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1


def search(alist, needle):
    alist_copy = list(alist)
    get_list_original_indices(alist)
    merge_sort(alist_copy)

    return _search(alist_copy, needle)

def _search(alist, needle):
    """Return the index of the found item. If not found return -1."""
    if len(alist) == 0:
        return -1

    mid = len(alist) // 2

    if needle == alist[mid]:
        return ORIGINAL_INDICES.get(needle, -1)

    else:
        if needle < alist[mid]:
            return _search(alist[:mid], needle)

        else:
            return _search(alist[mid + 1:], needle)


class TestSearchTestCase(unittest.TestCase):
    """Tests for search method."""
    def test_list(self):
        alist =[1, 3, 2, 0]
        self.assertEqual(search(alist, 2), 2)
        self.assertEqual(search(alist, 0), 3)

    def test_tuple(self):
        alist =(1, 3, 2, 0)
        self.assertEqual(search(alist, 2), 2)
        self.assertEqual(search(alist, 0), 3)



if __name__ == "__main__":
    # The total runtime is O(n log n)
    unittest.main()