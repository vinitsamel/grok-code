
def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        #print (str[i])
        if not str[i].isalpha():
            #print ("Not Alpha")
            continue
        else:
            capchar = str[i].capitalize()
            #print (capchar)
            #print (permutations)
            permLen = len(permutations)
            for j in range(permLen):
                perm = permutations[j]
                newString = perm[:i] + capchar + perm[i+1:]
                #print (newString)
                permutations.append(newString)
    return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
