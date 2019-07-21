def make_squares(arr):
    squares = []
    positiveFinder = 0
    negativeFinder = 0
    firstFlag = True
    while positiveFinder < len(arr) or negativeFinder
        if arr[positiveFinder] >= 0:
            if firstFlag:
                negativeFinder = positiveFinder - 1
                firstFlag = False
            if arr[negativeFinder] < 0:
                if arr[negativeFinder]**2 <= arr[positiveFinder]**2:
                    squares.append(arr[negativeFinder]**2)
                    negativeFinder -= 1
            squares.append(arr[positiveFinder] ** 2)
        positiveFinder += 1
    return squares

def main():
  print("Squares: " + str(make_squares([-1, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()