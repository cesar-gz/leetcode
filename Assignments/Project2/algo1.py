"""
Submission for Cesar Gutierrez
"""

def targetTermsOrSubstrings( cities:list[str], target:list[str] ) -> list[int]:
    """
    Given an array that is a single concatenation of some notable cities in California and a
    second array contains names of some real or imaginary cities, that may be present in the first array.
    Output an array containing starting indices of the target words in array one. All words are in small letters.
    """
    listOfArrays = []
    with open("in2a.txt", "r", encoding="utf8") as file:
        next(file)                                  # skip the first two lines
        next(file)                                  
        for line in file:
            line = line[13:-3]                      # get rid of "array 1a" and "\n"
            listOfArrays.append(line)
    
    listOfCities = []
    listOfTargets = []

    i = 2                                           # start removing the empty elements
    while i < len(listOfArrays):
        listOfArrays.pop(i)
        listOfArrays.pop(i)
        i += 2

    for elem in listOfArrays:
        elem = list(elem)
        j = 1
        while j < len(elem):
            elem[0] += elem.pop(j) 
        print(elem)

    print(cities)
    print(target)

    output_order = []                               # what will we turn in
    output_array = []
    word = ""                                       # temporary string variable
    size = len(cities[0])                           # grab the length of the concatenated string
    index = 0                                       # what will get added to the output array when word is found

    while(index < size):                            # check the entire long word
        for char in cities[0]:                      # for every character in the long word
            word += char                            # add the character to the temp
            if word in target:                      # if temp is in the list target cities
                output_order.append(index)          # add the index to the output array because we found a target city in the long word
                output_array.append(word)           # save the word in the order it appeared
                break                               # break out of the loop once found to save time
        word=""                                     # reset the temp word back to empty
        cities[0] = (cities[0])[1:]                 # slice the first character of the concatenated long word
        index += 1                                  # increment index to keep track the position of the long word, is also the exit condition
        
    print(output_array)
    return output_order

"""
Test Case
"""
# Input:
A = ["thismetoaklandrialtofullertonmarcolongchinofresnovallejoclovissimithound"]
B = [ 'marco', 'clovis', 'rialto', 'oakland']

# Output: 
# Output_order = [ 7, 14, 29, 56]
# Output_array =[ 'oakland', 'riato', 'marco', 'clovis']
print(targetTermsOrSubstrings(A,B))
