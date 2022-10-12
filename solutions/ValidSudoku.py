class Solution:
    def isValidSudoku(self, board):
        # rule 1: row/col: 1-9
        # rule 2: 3*3 sub-box
        
        dict = {}
        for nr in range(1,10):
            dict[f'{nr}'] = []
        
        # append all numbers into the dict
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    dict[board[i][j]].append((i,j))
        
        # judge
        for nr in range(1,10):
            if dict[f'{nr}']:
                # rule 1
                list_i = []
                list_j = []
                list_ij = []
                for (i,j) in dict[f'{nr}']:
                    list_i.append(i)
                    list_j.append(j)
                    list_ij.append((i//3, j//3))
                if len(set(list_i)) < len(list_i) or len(set(list_j)) < len(list_j):
                    return False
                
                # rule 2
                if len(set(list_ij)) < len(list_ij):
                    return False
        
        return True

if __name__ == "__main__":
    sol = Solution()

    board_1 = [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

    print(sol.isValidSudoku(board_1))