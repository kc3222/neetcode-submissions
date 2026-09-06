class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Form a graph of words
        dct = defaultdict(list)
        def wordTransform(word):
            res = []
            for i in range(len(word)):
                temp = word
                temp = temp[:i] + "*" + temp[i + 1:]
                res.append(temp)
            return res

        for word in wordList:
            wordBranches = wordTransform(word)
            for branch in wordBranches:
                dct[branch].append(word)

        # BFS with visited
        # Visiting graph of words to find the next transformation
        stack = [beginWord]
        visited = set()
        pathCount = 0
        while stack:
            pathCount += 1
            newStack = []
            for word in stack:
                if word == endWord:
                    return pathCount
                wordBranches = wordTransform(word)
                for branch in wordBranches:
                    for newWord in dct[branch]:
                        if newWord not in visited:
                            newStack.append(newWord)
                            visited.add(newWord)
            stack = newStack
        return 0
