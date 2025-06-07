from typing import List

class Solution:
    def pacificAtlantic(self,heights:List[List[int]])->List[List[int]]:
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

