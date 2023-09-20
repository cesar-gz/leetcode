"""
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter
"""

class TrieNode:
    def __init__(self):
        self.children = {} # a is mapped to : a TrieNode
        self.word = False  # word will tell us if we are at the end of the word
                           # set to false by default

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char] # update our current
        current.word = True

    def search(self, word: str) -> bool:
        def DFS(index, rootNode):
          current = rootNode

          for i in range(index, len(word)):
              char = word[i]

              if char == ".":
                  for child in current.children.values():
                      # because the dot can be any char, recursively call depth first search
                      if DFS(i + 1, child):
                          return True
                  return False

              else:
                  if char not in current.children:
                      # this char does DNE
                      return False
                  current = current.children[char]
          return current.word

        return DFS(0, self.root)
