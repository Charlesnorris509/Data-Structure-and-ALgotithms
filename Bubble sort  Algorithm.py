#This is the code for a bublle sort algorithm
# @CharlesNorris 7/03/21

class BubbleSort(object):

    def __init__(self, list):
        self.list = list
        self.sorted = self.bubble_sort()

    def str(self):
        return str(self.sorted)

    def  bubble_sort(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.list) - 1):
                if self.list[i] > self.list[i -1]:
                    self.list[i], self.list[i -1] = self.list[i -1], self.list[i]
        return self.list

if __name__=='__main__':
    print(BubbleSort([9, 4, 7, 5, 8, 3, 1]))
