from __future__ import print_function

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def isOverlap(intervalOne, intervalTwo=None):
    retVal = False
    if (intervalTwo or intervalOne) == None:
        retVal = False
    elif intervalOne.start in range(intervalTwo.start, intervalTwo.end) or \
        intervalOne.end in range(intervalTwo.start, intervalTwo.end) or \
        intervalTwo.start in range(intervalOne.start, intervalOne.end) or \
        intervalTwo.end in range(intervalOne.start, intervalOne.end):
        retVal = True
    return retVal

# Merge Intervals if overlap, if not return original interval
def mergeIntervals(intervalOne, intervalTwo):
    merged = Interval(0,0)
    if not isOverlap(intervalOne, intervalTwo):
        merged = intervalOne
    else:
        newStart = min(intervalOne.start, intervalTwo.start)
        newEnd   = max(intervalOne.end, intervalTwo.end)
        merged = Interval(newStart, newEnd)
    return merged

def mergeMess(intervals):
  intervals.sort(key=lambda x: x.start)

  merged = []
  i = 0
  while i < (len(intervals)):
      intervalOne = intervals[i]
      print ("\n ------ i: ")
      intervalOne.print_interval()
      for j in range (i+1, len(intervals)):
          print ("\nj : ")
          intervals[j].print_interval()
          mergedInterval = mergeIntervals(intervalOne, intervals[j])
          print ("\nmergedOne: ")
          mergedInterval.print_interval()
          if mergedInterval == intervalOne:
              print ("\nAppending Merge")
              merged.append(mergedInterval)
              i += 1
              break
          else:
              intervalOne = mergedInterval
      i += 1
  return merged

def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # sort the intervals on the start time
  intervals.sort(key=lambda x: x.start)

  mergedIntervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval.start <= end:  # overlapping intervals, adjust the 'end'
      end = max(interval.end, end)
    else:  # non-overlapping interval, add the previous internval and reset
      mergedIntervals.append(Interval(start, end))
      start = interval.start
      end = interval.end

  # add the last interval
  mergedIntervals.append(Interval(start, end))
  return mergedIntervals

def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()