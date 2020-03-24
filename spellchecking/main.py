"""
this project checks spelling of words and find three suggestions
"""
import difflib



def binarysearch(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid = (first+last) // 2

        if alist[mid] == item:
            return (True,0)
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1


    return (False, first )


def bestmatch(word, alist):
    sol = []
    for w in alist:
        r = difflib.SequenceMatcher(None, word, w).quick_ratio()
        if len(sol) < 5:
            sol.append((r, w))
        else:
            lowestmatch = 1
            lowestindex = 0
            for i in range(5):
                if lowestmatch > sol[i][0]:
                    lowestindex = i
                    lowestmatch = sol[i][0]
            if r > lowestmatch:
                sol[lowestindex] = (r, w)
    return sol


dictionaryfile = open("Dictionary.txt", "r").read()
dictionary = dictionaryfile.split()
text = input()
listOfWords = text.split()
for word in listOfWords:
    found , pos = binarysearch(dictionary, word)
    if not found :
        print("not correct word : ", word, end="")
        sol = bestmatch(word,dictionary)
        sol.sort()
        sol.reverse()
        print("suggestions :")
        for w in sol:
            print(w[1])
        new = input("do you want to add the word to dictionary ?  *press y to add it * : ")
        # print(pos)
        if new == "y" :
            dictionary.insert(pos,word)
            # print(dictionary[pos-1] , dictionary[pos],dictionary[pos+1])
