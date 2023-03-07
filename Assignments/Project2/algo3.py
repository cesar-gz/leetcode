"""
Submission for Cesar Gutierrez
"""
def mergeTechnique(input:list[int] ) -> list[int]:
    """
    Merge the various lists into a single sorted array
    """
    megaArray = []
    for list in input:
        megaArray += list
    megaArray = sorted(megaArray)
    return megaArray

"""
Test Cases:
"""

# Output : [ -10, -1, 0, 2, 2, 4, 5, 6, 9, 12, 20, 21, 81, 121, 150]
Array_1  =[ [2, 5, 9, 21],
	       [-1, 0, 2],
	       [-10, 81, 121],
	       [4, 6, 12, 20, 150] ]
print(mergeTechnique(Array_1))

# Output : [-3, 0, 3, 7, 8, 9, 10, 11, 11, 12, 17, 18, 19, 21, 29, 29, 81, 88, 121, 131]
Array_2  =[ [10, 17, 18, 21, 29],
	       [-3, 0, 3, 7, 8, 11],
	       [81, 88, 121, 131],
	       [9, 11, 12, 19, 29] ]
print(mergeTechnique(Array_2))

# Output: [-4, -2, 0, 2, 4, 5, 6, 6, 7, 10, 10, 12, 14, 15, 20, 24, 25]
Array_3  =[ [-4, -2, 0, 2, 7],
	       [4, 6, 12, 14],
	       [10, 15, 25],
	       [5, 6, 10, 20, 24] ]
print(mergeTechnique(Array_3))