class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row=len(heights)
        col=len(heights[0])
        result=[]
        pacific=set()
        atlantic=set()
        def dfs(r,c,ocean):
            ocean.add((r,c))

            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=row or nc<0 or nc>=col:
                    continue
                if (nr,nc) in ocean:
                    continue
                if heights[nr][nc]<heights[r][c]:
                    continue
                
                dfs(nr,nc,ocean)
        
        # Pacific->top+left
        for r in range(row):
            dfs(r,0,pacific)
        
        for c in range(col):
            dfs(0,c,pacific)
        
        # Atlantic->bottom+right
        for r in range(row):
            dfs(r,col-1,atlantic)
        
        for c in range(col):
            dfs(row-1,c,atlantic)
        
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
    