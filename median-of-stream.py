from heapq import *

class MedianOfAStream:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.numcount = 0

    def insert_num(self, num):
        if (self.numcount % 2) == 0:
            if len(self.minheap) == 0



    return -1

  def find_median(self):
    # TODO: Write your code here
    return 0.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
