#This code is gonna be the implementation of a Selection Sort algorithm with recusrive iteration
# @charlesnorris the 1/1/2021

class SelectionSortRecursion:

    def __init__(self, nums):
        self.nums = nums


    def find_mind(self, a, i, j):
        if i == j:
            return i
        z = self.find_mind(a, i +1, j)
        return i if a[i] < a[z] else z

    def sort(self):
        self.selection_sort(self.nums)

    def selection_sort(self, nums, actual_index=0):
        if actual_index == len(nums):
            return 
        if min_index != actual_index:
            nums[min_index], nums[actual_index] = nums[actual_index], nums[min_index]
        selection_sort(nums, actual_index + 1)

if __name__ == '__main__':
    n = [1, 5, 3, 4, 2, 8, 9, 7, 6]
    print(n)
    sort = SelectionSortRecursion()
    sort.sort()
    print(sort.nums)

