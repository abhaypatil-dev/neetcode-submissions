class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Sets
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxs = [set() for _ in range(n)]

        # Traverse
        for r in range(n):
            for c in range(n):
                ch = board[r][c]
                if ch == '.': continue

                # Rows, Cols, Boxes
                if ch in rows[r]: return False
                rows[r].add(ch)
                if ch in cols[c]: return False
                cols[c].add(ch)
                boxnum = (n//3)*(r//3) + c//3
                # print(boxnum)
                if ch in boxs[boxnum]: return False
                boxs[boxnum].add(ch)
        
        return True