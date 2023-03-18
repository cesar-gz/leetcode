"""
Submission for Cesar Gutierrez
"""
def mergeTechnique():
    """
    Given the input text file, merge the various lists
	into a single sorted ascending array
    """
    megaArray = []
    subString1 = "] ]"
    subString2 = "],"
    
	# begin parsing the text file
    with open("in2C.txt", "r", encoding="utf8") as file:
        temp = []
        next(file)                             			# skip first two lines
        next(file)
        for line in file:								
            if line[0] == 'A':							# get rid of "Array_X ["
                line = line[12:]
                if len(temp) != 0:						# if we are at the next input array
                    megaArray.append(temp)				# save current temp array
                    temp = []							# reset the temp array
            i = 0
            for char in line:
                # start taking characters until we hit the end of the given array
                if i < len(line)-1 and (line[i] + line[i+1] != subString1 or subString2):
                    if char == "[" or char == "]" or char == " " or char == "\t":
                        # ignore these characters and move on until we hit a number
                        i += 1
                        continue
                    # a number or negative symbol was found, add it
                    temp.append(char)
                i += 1
            #print(line)
        else:										# if we are at the last input array
            megaArray.append(temp)					# save current temp array

	# convert string list into int list
    i = 0
    for array in megaArray:
        temp = ""
        for elem in array:                          # concatenate the array of chars into one string
            temp += elem
        temp = temp.split(",")                      # split the string into a list of numbered strings
        j = 0
        for elem in temp:                           
            temp[j] = int(elem)                     # convert string elements to int elements in array
            j += 1
        megaArray[i] = temp
        i += 1
    
    # start sorting the arrays
    for array in megaArray:
        size = len(array)                           # implementing a simple bubble sort
        for p in range(size):
            flag = True                             # used to cut the sorting alg short if nothing left to sort
            for q in range(size - p - 1):
                if array[q] > array[q+1]:
                    array[q], array[q+1] = array[q+1], array[q]         # in place swap
                    flag = False
            if flag == True:                        # if no swaps were done, then move on
                break
    return megaArray

"""
Test Cases:
"""
# input is a file in the same directory as this py file
mergedArray = mergeTechnique()
print("the resulting merged lists are: ")
for elem in mergedArray:
    print(elem)