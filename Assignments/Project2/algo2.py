"""
Submission for Cesar Gutierrez
"""

def stringRunEncoder(string) -> str:
    """
    A "run" is a substring of repeated characters, for example "aaaa". Run-length encoding means 
    replacing all similar characters with a single copy of the character and a count of how
    many times it appears. "aaaa" is replaced with "4a". Input: A string of n characters that are
    lowercase or a spaces. Output: a string with runs
    """
    slicedStr = string[1:]
    newString = ""
    counter = 1
    index = 0
    i = 0

    for char in string:
        while string[i] == slicedStr[i]:
            slicedStr = slicedStr[1:]
            i += 1
            counter += 1
        index += 1
        i = index
        newString += str(counter) + char
        counter = 1 

    newString = newString.replace("1", "")

    return newString        

"""
    count = {}                                      # tracks each characters occurence in the string
    for char in string:                             # for every character in the input string
    count[char] = 1 + count.get(char, 0)        # if the char doesn't exist in dictionary, then default value is 0, otherwise increment by 1
"""

"""
Test Cases
"""
str2 = "heloooooooo there" 
# Outout: "hel8o there"
print(stringRunEncoder(str2))

str1 = "ddd" 
# Output: "3d"
print(stringRunEncoder(str1))

str3 = "choosemeeky and tuition-free" 
# Output: "ch2osem2eky and tuition-fr2e"
print(stringRunEncoder(str3))