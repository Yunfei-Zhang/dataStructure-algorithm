class Solution:
    def findDiagonalOrder(self, mat):
        # define the boundary of matrix
        m = len(mat)
        n = len(mat[0])
        output = []

        if m == 1:
            return mat[0]
        
        # define the range of the sum of row and col indices
        for i in range(m+n-1):  # each diagonal line
            if i == 0:
                output.append(mat[0][0])
            elif i % 2 != 0:
                for row in range(i+1):
                    col = i - row
                    if col > n-1 or row > m-1:
                        continue
                    output.append(mat[row][col])
            else:
                for row in range(i,-1,-1):
                    col = i - row
                    if col > n-1 or row > m-1 or col < 0:
                        continue
                    output.append(mat[row][col])
        return output

if __name__ == "__main__":
    sol = Solution()
    # test 1
    ans = sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
    # # test 6
    # ans = sol.findDiagonalOrder([[6,9,7]])
    # # test 15
    # ans = sol.findDiagonalOrder([[2,5],[8,4],[0,-1]])
    # test 24
    ans = sol.findDiagonalOrder([list(range(1,10001))])
    print(ans)