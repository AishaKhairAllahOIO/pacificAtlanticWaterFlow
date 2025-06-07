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
        return coordinates
    


