"""
Submission for Cesar Gutierrez
"""

def matchingGroupSchedules(person1_DA, person1_Sch, person2_DA, person2_Sch, duration_of_meeting):
    """
    Taking at least two different group members, output an array that displays available time meetings based
    on the input of their Daily Activities(array), Schedules(array), and duration they want the meeting to be.
    Daily Activities is the non available times, and Schedules is the complete time a person could meet
    """

    # change arrays into integers and remove the semicolon
    # O( a^2 * b^2 * c * d)
    for i in range(len(person1_DA)):
        for j in range(len(person1_DA[i])):
          person1_DA[i][j] = int(person1_DA[i][j].replace(':',''))
    for i in range(len(person2_DA)):
        for j in range(len(person2_DA[i])):
          person2_DA[i][j] = int(person2_DA[i][j].replace(':',''))
    for i in range(len(person1_Sch)):
      person1_Sch[i] = int(person1_Sch[i].replace(':', ''))
    for i in range(len(person2_Sch)):
      person2_Sch[i] = int(person2_Sch[i].replace(':', ''))

    # combine the two, person1_DA will be our working array we will manipulate
    person1_DA += person2_DA
    # n log n sort
    person1_DA.sort()

    # find the time window that both members are available at the same time
    person1_Sch[0] = max(person1_Sch[0], person2_Sch[0])
    person1_Sch[1] = min(person1_Sch[1], person2_Sch[1])

    # removes times that are outside of the members regular schedule
    for row in person1_DA:
       if row < person1_Sch:
          person1_DA.remove(row)
       if row[0] > person1_Sch[1]:
          person1_DA.remove(row)

    # create output array
    answer = []

    # append to output array only the times of the daily activities that meet the duration_of_meeting
    for i in range(len(person1_DA) - 1):
        if person1_DA[i][1] < person1_DA[i+1][0]:
            if (person1_DA[i+1][0] - person1_DA[i][1]) >= duration_of_meeting:
              answer.append([person1_DA[i][1],person1_DA[i+1][0]])

    # add to the beginning of the output array any free time both could meet that follows the d_of_m & time window schedule
    if (person1_DA[0][0] - person1_Sch[0]) >= duration_of_meeting:
       answer.insert(0, [person1_Sch[0], person1_DA[0][0]])

    # add to the end of the output array any free time both could meet that follows the d_of_m & time window schedule
    if ( person1_Sch[1] - person1_DA[ len(person1_DA) - 1][1] ) >= duration_of_meeting:
       answer.append([person1_DA[ len(person1_DA) -1 ][1], person1_Sch[1]])

    # format the output array back to string, and add the semicolon in the correct index
    for i in range(len(answer)):
       for j in range(len(answer[i])):
          answer[i][j] = str(answer[i][j])
          answer[i][j] = (answer[i][j])[:-2] + ':' + (answer[i][j])[-2:]

    return answer


"""
Test Case
"""
person1_DailyActivity = [['7:00', '8:30'],  ['12:00', '13:00'],  ['16:00', '18:00']]
person2_DailyActivity = [['9:00', '10:30'],  ['12:20', '14:30'],  ['14:00', '15:00'], ['16:00', '17:00']]

person1_Schedule = ['9:00', '19:00']
person2_Schedule = ['9:00', '18:30']

duration_of_meeting = 30

result = matchingGroupSchedules(person1_DailyActivity, person1_Schedule, person2_DailyActivity,person2_Schedule, duration_of_meeting)
print(result)
