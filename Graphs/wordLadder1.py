"""
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from beginWord to endWord,
or 0 if no such sequence exists.

"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        wordSet = set(wordList+[beginWord])

        # create a graph with helper function
        graph = defaultdict(set)
        for s in wordList+[beginWord]:
            for i in range(len(s)):
                # create two temporary words
                temp1, temp2 = s[0:i], s[i+1:]
                for a in alphabet:
                    temp = temp1 + a + temp2
                    if temp in wordSet and temp!= s:
                        graph[s].add(temp)

        # BFS queue (track steps in the queue)
        q = deque( [(beginWord, 0)] )     # 0 is the amount of steps so far
        visited = set()

        # if we can find end word, then return number of steps to get there
        while q:
            node, step = q.popleft()

            if node == endWord: return step+1

            if node not in visited:
                visited.add(node)
                for nextNode in graph[node]:
                    if nextNode not in visited: q.append((nextNode, step+1))

        return 0
    # Time (N x M x 26)
