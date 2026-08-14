class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                curr[c] = {}
                curr = curr[c]
        curr["#"] = {}
        return

    def search(self, word: str) -> bool:
        curr = self.trie
        
        def dfs(dct, idx):
            if idx == len(word):
                if "#" in dct:
                    return True
                return False
            if word[idx] == ".":
                for key in dct:
                    path = dfs(dct[key], idx + 1)
                    if path:
                        return True
                return False
            elif word[idx] not in dct:
                return False
            else:
                return dfs(dct[word[idx]], idx + 1)

        return dfs(curr, 0)