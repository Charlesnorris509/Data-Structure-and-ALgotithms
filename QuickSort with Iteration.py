"""This is the code for a quicksort algorithm implementated via iteration
in python (Abstract Data Structure + Sorting Algorithm)
@Charles Norris 28/02/2021 """

from collections import deque

class QuickSortIter:

    def __init__(self, data):
        self.data = data

    def partition(self, low, high):
        pivot_index = (low + high)
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for j in range(low, high, 1):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1

        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low

    def sort(self):
        stack = deque()
        stack.append((0, len(self.data) - 1))
        while stack:
            start, end = stack.pop()
            pivot = self.partition(start, end)
            if pivot - 1>  start:
                stack.append((start, pivot - 1))
            if pivot + 1 < end:
                stack.append((pivot + 1, end))


if __name__ == '__main__':
    n = [10,9,8,7,6,5]
    sort = QuickSortIter()
    sort.sort()
    print(sort.data)