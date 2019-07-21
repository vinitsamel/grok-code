def search_next_letter(letters, key):
    start, end = 0, len(letters)-1
    if key < letters[start] or key > letters[end]:
        return letters[0]
    while start <= end:
        mid = int((start + end) / 2)
        print (start, end, mid)
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % len(letters)]

def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
