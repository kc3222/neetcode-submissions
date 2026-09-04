class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Build a trie
        trie = {}
        for word in wordDict:
            if word[0] not in trie:
                trie[word[0]] = []
            trie[word[0]].append(word)

        memo = {}
        # Search the dict
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            if s[i] in trie:
                words = trie[s[i]]
                for word in words:
                    if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                        if dfs(i + len(word)):
                            memo[i] = True
                            return True
            memo[i] = False
            return False
        
        return dfs(0)