#This is the implementation of a Counting Sort Algorithm in Python

class CountSort:
  
  def __init__(self, data):
    self.data = data
    #count = max - min + 1
    self.count = [0 for i in range(max(data) - min(data) + 1)]
    
  def sort(self):
    for i in range(len(self.data)):
      self.count[self.data[i] - min(data)] += 1
    #We have consider the count variable 0(k)
    
    y = 0
    for i in range(min(self.data), max(self.data)+1):
      while self.count[i - min(self.data)] > 0:
        self.data[y] = i
        y += 1
        self.count[i - min(self.data)] -= 1
        
        
if __name__ == '__main__':
  n = [ 1, 5, 8, 9, -1, -4]
  counting_sort = CountSort(n)
  counting_sort.sort()
  print(counting_sort.data)
