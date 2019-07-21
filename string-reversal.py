def reverseString(inputString):
    chars = list(inputString)
    leftPointer = 0
    rightPointer = len(inputString)-1
    while(leftPointer < rightPointer):
        chars[leftPointer], chars[rightPointer] = chars[rightPointer], chars[leftPointer]
        leftPointer += 1
        rightPointer -= 1
    return ''.join(chars)

def reverseString2(inputString):
    return ''.join(reversed(inputString))

def isPalindrome(inputString):
    return reverseString(inputString) == inputString

def sortedString(inpString):
    chars = list(inpString)
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            if chars[i] > chars[j]:
                chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)

def isAnagram(stingOne, stringTwo):
    return sortedString(stingOne) == sortedString(stringTwo)

def main():
    print (reverseString2("reverse"))
    print (isPalindrome("reverse"))
    print (reverseString2("nitin"))
    print (isPalindrome("nitin"))
    print (sortedString("sandiegozoo"))
    print (isAnagram("cinema", "iceman"))
    print (isAnagram("length", "yard"))

main()