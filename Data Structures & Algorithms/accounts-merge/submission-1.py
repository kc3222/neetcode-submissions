class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Union every account that shares an email with an earlier one
        owner = {}  # email -> first account index that had it
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in owner:
                    union(i, owner[email])
                else:
                    owner[email] = i

        # Bucket emails by their root account
        groups = defaultdict(list)
        for email, i in owner.items():
            groups[find(i)].append(email)

        return [[accounts[root][0]] + sorted(emails)
                for root, emails in groups.items()]