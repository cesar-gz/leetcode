"""
355. Design Twitter
Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user themself.
Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
"""

class Twitter:

    def __init__(self):
        # counting our number of tweets
        self.count = 0
        # map each user to a list of that users tweets, and as well to the count [count, tweetIds]
        self.tweetMap = defaultdict(list)
        # maintain a user and the set of all the people they follow
        self.followMap = defaultdict(set) # hash set


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append( [self.count, tweetId] )
        self.count -= 1 # decrement instead of increment because we are using a minHeap and have to reverse positive with negative

    def getNewsFeed(self, userId: int) -> List[int]:
        # our list of tweets to return to the user, ordered from recent
        result = []
        # help figure out the most recent tweets
        minHeap = []

        # since each user follows themselves, add them to the most recent tweets
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            # if they have at least one tweet
            if followeeId in self.tweetMap:
              index = len(self.tweetMap[followeeId]) - 1
              count, tweetId = self.tweetMap[followeeId][index]
              minHeap.append( [count, tweetId, followeeId, index - 1] )

        # turn list to Heap
        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            # if they still have tweets
            if index >= 0:
              count,tweetId = self.tweetMap[followeeId][index]
              heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
          self.followMap[followerId].remove(followeeId)
