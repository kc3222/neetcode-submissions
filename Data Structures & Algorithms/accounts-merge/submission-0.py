class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union Find
        mailsDct = {}
        accountsParent = [i for i in range(len(accounts))]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False # already connected
            accountsParent[x] = accountsParent[y]
            return True
        
        def find(x):
            if accountsParent[x] != x:
                accountsParent[x] = find(accountsParent[x])  # path compression
            return accountsParent[x]
        
        # Build and search
        for i in range(len(accounts)):
            # Loop through each account
            mails = accounts[i][1:]
            name = accounts[i][0]
            for mail in mails:
                if mail not in mailsDct:
                    mailsDct[mail] = i
                else:
                    union(i, mailsDct[mail])
        
        # Return result
        result = defaultdict(list)
        for mail in mailsDct:
            idx = accountsParent[mailsDct[mail]]
            result[idx].append(mail)
        res = []
        for idx in result:
            name = accounts[idx][0]
            res.append([name] + result[idx])
        return res