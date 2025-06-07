from typing import List

class Solution:
    def pacificAtlantic(self,heights:List[List[int]])->List[List[int]]:
        ROWS,COLUMNS=len(heights),len(heights[0])
        pacific,atlantic=set(),set()
