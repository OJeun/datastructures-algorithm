class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        horizontal = len(grid[0]) # 5
        vertical = len(grid) # 4

        self.grid = grid
        islands = 0

                # change 1 to 0 of lands in an island
        def dfs(v, h):
            if v < 0 or v >= vertical or h < 0 or h >= horizontal:
                return

            if self.grid[v][h] == "0":
                return
            
            self.grid[v][h] = "0"

            up = dfs(v-1, h)
            down = dfs(v+1, h)
            right = dfs(v, h+1)
            left = dfs(v, h-1)

        # O(n^2) for loop to iterate 2D array to find a 1(land)
        for m in range(vertical): 
            for n in range(horizontal):
                if self.grid[m][n] == "1":
                    islands += 1
                    dfs(m, n)

        return islands

# 핵심 아이디어
# grid를 한 칸 한 칸 순회한다.

# '1'을 발견하면 → 새로운 섬을 찾은 거다 → 섬 개수 +1

# '1'을 발견했으면, 그 섬에 연결된 모든 '1'들을 DFS로 전부 방문해서 '0'으로 바꾼다. (이미 방문한 것처럼 표시)

# 이렇게 하면 같은 섬을 두 번 세지 않는다.

# = 연결된 모든 '1'을 한번에 지워버리기 (방문 처리)