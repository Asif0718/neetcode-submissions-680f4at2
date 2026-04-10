class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bruteforce
        '''for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False'''

        row , col = len(matrix) , len(matrix[0])

        top , bot = 0 , row-1

        while top<=bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not(top<=bot):
            return False

        row = (top+bot)//2
        l , r = 0 , col-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False                                    
