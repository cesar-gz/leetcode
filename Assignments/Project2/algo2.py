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
    newString = ""
    copy = string

    for i in range( len(string) -1 ):
        counter = 1
        if string[i] == string[i+1] and i < len(string):
            counter += 1
        newString += str(counter) + copy[i]

    newString = newString.replace("1", "")

    return newString


"""
Test Cases
"""
str1 = "ddd"
# Output: "3d"
print(stringRunEncoder(str1))

str2 = "heloooooooo there"
# Output: "hel8o there"
print(stringRunEncoder(str2))

str3 = "choosemeeky and tuition-free"
# Output: "ch2osem2eky and tuition-fr2e"
print(stringRunEncoder(str3))
