class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.offsets = [(0,1),(0,-1),(-1,0),(1,0)]
        m = len(heights) # vertical length
        n = len(heights[0]) # horizontal length
        solutions = []
        pacificArr = [ [False]*n for i in range(m)]
        atlanticArr = [ [False]*n for i in range(m)]

        # do dfs for solutions
        for i in range(n):
            self.dfs(0,i,m,n,heights,pacificArr)
            self.dfs(m-1,i,m,n,heights,atlanticArr)

        for i in range(m): 
            self.dfs(i,0,m,n,heights,pacificArr)
            self.dfs(i,n-1,m,n,heights,atlanticArr)    
        
        # collect final solutions
        for row in range(m):
            for col in range(n):
                if pacificArr[row][col] and atlanticArr[row][col]:
                    solutions.append([row,col])
        return solutions

    def dfs(self, row: int, col: int,m: int,n: int, heights: List[List[int]], board: List[List[bool]]):
        board[row][col] = True
        for (x,y) in self.offsets:
            row2 = row+x
            col2 = col+y
            # If we can go to this offset
            if self.canReach(row,col,row2,col2,m,n,heights):
                if not board[row2][col2]: 
                    self.dfs(row2,col2,m,n,heights,board)

    def canReach(self, row: int, col: int, row2: int, col2: int, m: int, n: int, heights: List[List[int]]) -> bool:
        if row2 < m and row2 >= 0 and col2 < n and col2 >= 0:
            return heights[row][col] <= heights[row2][col2]
        return False

# O(mn) space, O(mn) time




