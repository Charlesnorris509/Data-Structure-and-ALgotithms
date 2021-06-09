#This is the implementation of an Insertion Sorting Algorithm 

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        
        while j > 0 and nums[j -1] > nums[j]:
            nums[j -1], nums[j] = nums[j], nums[j -1]
            j =j -1


if __name__ == '__main__':
    x = [15, 20, 4, 9, 5, 18]
    insertion_sort(x)