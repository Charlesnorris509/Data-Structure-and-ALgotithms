#This is the Implementation of a sortinng algorithm using python
#BogoSort @CharlesNorris

import random

class Bogosort:

    def __init__(self, nums):
        self.nums = nums

    def is_sorted(self):
        for i in range(self.nums - 1):
            if self.nums[i] > self.nums[i + 1]:
                return False
        return True

    def shuffle(self):
        for i in range(len(self.nums)- 2, 0, -1):
            j = random.randint(0,i +1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sort(self):
        while not self.is_sorted():
            print('Shuffle Again....')
            self.shuffle()

if __name__ == '__main__':
    bg = Bogosort([2, -5, 8, 50, -45, 3,  6, 9, 15])
    bg.sort()
    print(bg.nums)