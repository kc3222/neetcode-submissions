class PrefixTree:

    def __init__(self):
        self.dct = {}

    def insert(self, word: str) -> None:
        curr = self.dct
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                curr[c] = {}
                curr = curr[c]
        curr['#'] = True

    def search(self, word: str) -> bool:
        curr = self.dct
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                return False
        if '#' in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.dct
        for c in prefix:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return True
        