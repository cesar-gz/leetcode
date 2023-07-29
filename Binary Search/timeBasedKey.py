"""
981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values
for the same key at different time stamps and retrieve the key's value at
a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.

void set(String key, String value, int timestamp) Stores the key with
the value value at the given time timestamp.

String get(String key, int timestamp) Returns a value such that
set was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the value associated
with the largest timestamp_prev. If there are no values, it returns "".
"""


class TimeMap:

    def __init__(self):
        # key: string, value: [ list of pairs[value,time stamp]]
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            # insert key
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        output = ""

        # get our list of values. If the key DNE, initialize it to a empty list
        values = self.hashMap.get(key, [])

        # start binary search
        leftPtr, rightPtr = 0, len(values) - 1
        while leftPtr <= rightPtr:
            middle = (leftPtr + rightPtr) // 2
            if values[middle][1] <= timestamp:
                # the closest timestamp we have seen so far
                output = values[middle][0]
                # we want to search right portion now
                leftPtr = middle + 1
            else:
                rightPtr = middle - 1

        return output



        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)
