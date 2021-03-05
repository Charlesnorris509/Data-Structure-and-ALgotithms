#This is the implementation of a TimSort Algorithm using python
# @CharlesNorris the 5/03/2021

import random

class TimSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        self.merge_sort(self.data)

    def  merge_sort(self, nums):
         if len(nums) <= 64:
             self.insertion_sort(nums)
             return nums

         middle_index = len(nums) // 2
         left_half = nums[:middle_index]
         right_half = nums[middle_index:]

         self.merge_sort(left_half)
         self.merge_sort(right_half)

         i = 0
         j = 0
         k = 0 

         while i < len(left_half) and j < len(right_half):
             if left_half[i] < right_half[j] :
                 nums[k] = left_half[i]
                 i += 1
             else :
                 nums[k] = right_half[j]
                 j += 1

             k += 1

         while i < len(left_half):
             nums[k] = left_half[i]
             i += 1
             k += 1

         while j < len(right_half):
             nums[k] = right_half[j]
             j += 1
             k += 1

    def insertion_sort(sub_array):
        for i in range(len(sub_array)):
            j = i
            while j > 0 and sub_array[j - 1] > sub_array[j]:
                sub_array[j -1], sub_array[j] = sub_array[j], sub_array[j -1]
                j -= 1

if __name__ == '__main__' :
    n = [n for n in range(100000)]
    random.shuffle(n)
    sort = Timsort(n)
    sort.sort()
    print(sort.data)

