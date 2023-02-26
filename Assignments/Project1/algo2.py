"""
Pseudocode:

create answer array

get the combinedSize of DAArray1 and DAArray2, add them together

sort answer array

then from here remove the elements that do fit within the opposite ends of the schedule array
then start popping/removing elements that when subtracted dont fit the duration of the meeting

"""

def matchingGroupSchedules(person1_DA, person1_Sch, person2_DA, person2_Sch, duration_of_meeting):
    """
    Taking at least two different group members, output an array that displays available time meetings based
    on the input of their Daily Activities(array), Schedules(array), and duration they want the meeting to be.
    Daily Activities is the non available times, and Schedules is the complete time a person could meet
    """

    # change both arrays into ints and remove the semicolon
    # n^2 total I believe for two arrays of size n
    for i in range(len(person1_DA)):
        person1_DA[i] = int(person1_DA[i].replace(':',''))

    for i in range(len(person2_DA)):
        person2_DA[i] = int(person2_DA[i].replace(':', ''))

    answer = person1_DA + person2_DA
    # n log n sort
    answer.sort()

    return answer

"""
Test Case
"""
person1_DA = ['7:00', '8:30',  '12:00', '13:00',  '16:00', '18:00']
person2_DA = ['9:00', '10:30',  '12:20', '14:30',  '14:00', '15:00', '16:00', '17:00']

person1_Sch = [9,19]
person2_Sch = [9,18.5]

duration_of_meeting = 30

result = matchingGroupSchedules(person1_DA, person1_Sch, person2_DA,person2_Sch, duration_of_meeting)
print(result)
