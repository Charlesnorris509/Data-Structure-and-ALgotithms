#This is the implementation of a Counting sort Algorithm in Python

class CountingSort:
  
  def __init__(self, data):
    self.data = data
    self.count = [0 for i in range(max(self.data) - min(self.data)+1)]
    
  def sort(self):
    for i in range(len(self.data)):
      self.count[self.data[i] - min(self.data)] += 1
      
    y = 0 
    for i in range(min(self.data), max(self.data)+1):
      while self.count[i- min(self.data)] > 0:
        self.data[y] = i
        y += 1
        self.count[i - min(self.data)] -= 1
        
        
        
if __name__ == '__main__':
  n = [1, 6, 3, 2, -3, -1, 8, 9, 42]
  count = CountingSort(n)
  count.sort()
  print(count.data)
