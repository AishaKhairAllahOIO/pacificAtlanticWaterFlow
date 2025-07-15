from pacificAtlanticWaterFlowVisual import visualSolution
from collections import deque

class Solution:

    def pacificAtlantic_DFS(self,heights):
    
        ROWS,COLUMNS=len(heights),len(heights[0])
        pacific,atlantic=set(),set()
        
        def DFS(r,c,visit,prevHeight):
            if(r,c)in visit or r<0 or c<0 or r==ROWS or c==COLUMNS or heights[r][c]<prevHeight:
                return            
            visit.add((r,c))
            DFS(r+1,c,visit,heights[r][c])
            DFS(r-1,c,visit,heights[r][c])
            DFS(r,c+1,visit,heights[r][c])
            DFS(r,c-1,visit,heights[r][c]) 

        for c in range(COLUMNS):
            DFS(0,c,pacific,heights[0][c])
            DFS(ROWS-1,c,atlantic,heights[ROWS-1][c])

        for r in range(ROWS):
            DFS(r,0,pacific,heights[r][0])
            DFS(r,COLUMNS-1,atlantic,heights[r][COLUMNS-1]) 

        coordinates=[]
        for r in range(ROWS):
            for c in range(COLUMNS):
                 if (r,c)in pacific and (r,c)in atlantic:
                    coordinates.append([r,c])
        return coordinates,pacific,atlantic
    
    def pacificAtlantic_BFS(self,heights):
        ROWS,COLUMNS=len(heights),len(heights[0])

        def BFS(starts):
            visited=set()
            queue=deque(starts)
            while queue:
                r,c=queue.popleft()
                visited.add((r,c))
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc=r+dr,c+dc
                    if (0<=nr<ROWS and 0<=nc<COLUMNS and(nr,nc) not in visited and heights[nr][nc]>=heights[r][c]):
                        queue.append((nr,nc))
            return visited

        pacific_starts=[(0,c)for c in range(COLUMNS)]+[(r,0) for r in range(ROWS)]
        atlantic_starts=[(ROWS-1,c) for c in range(COLUMNS)]+[(r,COLUMNS-1) for r in range(ROWS)]

        pacific=BFS(pacific_starts)
        atlantic=BFS(atlantic_starts)

        coordinates=[[r, c] for r in range(ROWS) for c in range(COLUMNS) if (r,c) in pacific and (r,c) in atlantic]
        return coordinates,pacific,atlantic

    

heights=[
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
sol=Solution()
answer,pacific,atlantic=sol.pacificAtlantic_BFS(heights)
# answer,pacific,atlantic=sol.pacificAtlantic_DFS(heights)
print(f"\n Total Pacific Reachable Cells: {len(pacific)}")
print(pacific,"\n")
print(f" Total Atlantic Reachable Cells: {len(atlantic)}")
print(atlantic,"\n")
print(f" Shared Cells (to both oceans): {len(answer)}")
print(answer,"\n")

visualSolution(heights,pacific,atlantic)