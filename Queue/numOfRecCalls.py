"""
933. Number of Recent Calls
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.

int ping(int t) Adds a new request at time t,
where t represents some time in milliseconds,
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
"""
class RecentCounter:

    def __init__(self):
        # create the new queue
        self.queue = deque()

    def ping(self, t: int) -> int:
        # when we get a ping, add the new ping to the queue
        self.queue.append(t)

        # remove all pings in queue with value more than 3000 away from new ping
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()

        return len(self.queue)

# O(N) time and space, we may need to remove N pings from queue or store N pings in our queue
