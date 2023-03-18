"""
Submission for Cesar Gutierrez
"""
def targetTermsOrSubstrings():
    """
    Given a text file that contains an array that is a single concatenation 
    of some notable cities in California, and a second array that contains 
    names of some real or imaginary cities, that may be present in the first array.
    Output an array containing starting indices of the target words in array one. 
    All words are in small letters.
    """
                                                        # begin parsing the text file
    listOfArrays = []
    with open("in2a.txt", "r", encoding="utf8") as file:
        next(file)                                      # skip the first two lines
        next(file)
        x = 1
        for line in file:                               # format every other array correctly
            if x%2 != 0:
                line = line[13:-3]                      # get rid of "array 1a" and "\n"
            elif x%2 == 0:
                line = line[12:-2]
            listOfArrays.append(line)                   # add to the mega list
            x += 1

    i = 2                                               # start removing the empty elements
    while i < len(listOfArrays):
        listOfArrays.pop(i)                             # will remove the empty lists[]
        listOfArrays.pop(i)
        i += 2

    listOfCities = []                                   # start separating the mega list
    listOfTargets = []
    x = 1

    for elem in listOfArrays:                           
        elem = list(elem)
        j = 1
        while j < len(elem):
            elem[0] += elem.pop(j)                      # grab the array 
        if x%2 != 0:                                    # place even numbered indices go cities array
            listOfCities.append(elem)
        elif x%2 == 0:                                  # place odd numbered indices go to targets array
            listOfTargets.append(elem)
        x += 1

    listOfArrays = listOfTargets                        # did this swapping process in a weird way
    listOfTargets = []                                  
    j = 0
    for elem in listOfArrays:                           
        temp = []
        for item in elem:
            if j == len(listOfArrays)-1:                # add a ' to the last element in the list
                item += "'"
            temp.append(item)
        j += 1
        listOfTargets.append(temp)                      
    
    p = 0
    for elem in listOfTargets:                          # grab the string element, remove the "" marks, splice it into a list
        listOfTargets[p] = list( elem[0].replace("'","").split(", ") )
        p += 1
                                                        # finished parsing the text file
    
    finalArray = []
    for i in range(len(listOfCities)):
        cities = listOfCities[i]                        # grab the current cities array
        target = listOfTargets[i]                       # grab the corresponding targets array

        output_order = []                               # the two lists we will print
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

        print("")
        print(output_order)
        print(output_array)
        finalArray.append(output_order)

    return finalArray

"""
Test Case
"""
# input is a file that is in the same directory as this py file
array = targetTermsOrSubstrings()