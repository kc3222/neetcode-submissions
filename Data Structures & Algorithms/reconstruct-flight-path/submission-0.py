class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build out degrees
        outDegrees = defaultdict(list)
        for ticket in tickets:
            outDegrees[ticket[0]].append(ticket[1])
        # Sort the out degrees
        for node in outDegrees:
            outDegrees[node] = sorted(outDegrees[node], reverse=True)
        # Start from JFK
        # DFS
        # Postorder then reverse
        res = []
        def dfs(node):
            if len(outDegrees[node]) == 0:
                res.append(node)
                return
            while outDegrees[node]:
                nxtNode = outDegrees[node].pop()
                dfs(nxtNode)
            res.append(node)
            return
        dfs("JFK")
        return res[::-1]