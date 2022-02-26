def longestWordLength(string):
    length = 0  # Initilize length to 0
    w = ''  # Initlize word to empty

    # Finding longest word in the given sentence and word
    for word in string.split():
        if (len(word) > length):
            length = len(word)
            w = word
    return (length, w)


string = input("Enter the string: ")
l, w = longestWordLength(string)
print("Longest word is ", w, " and its length is ", l)
