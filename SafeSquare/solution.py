def print_mat(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print('')

class chess:
    def __init__(self, mat):
        self.n = len(mat)
        self.m = len(mat[0])
        self.mat = mat
        self.result = [[1]*self.m]*self.n
        pass


    # TODO: CRIO_TASK_MODULE_SAFE_SQUARE
    # Input:
    #   1) chess board matrix
    # Task:
    #   1) Implement Rook move (hathi)
    #   2) Implement Bishop move (camel)
    #   3) Implement Queens move (vajir)
    #   4) Implement knight's move (horse)
    #   5) Special move (layer)
    # Output:
    #   Count the number of safe square and return it
    def up(self,i,j,result,limit,jump = True):
        k = 0
        for i in range(i,limit - 1,-1):
            if(not jump):
                if(k and self.mat[i][j] != '.'):
                    break
                k = 1
            print(i)
            result[i][j] = 0
        return result
                 


    def down(self,i,j,result,limit,jump = True):
        k = 0
        for i in range(i,limit + 1):
            if(not jump):
                if(k and self.mat[i][j] != '.'):
                    break
                k = 1
            result[i][j] = 0
        return result
        
    def right(self,i,j,result,limit,jump = True):
        k = 0
        for j in range(j,limit + 1):
            if(not jump):
                if(k and self.mat[i][j] != '.'):
                    break
                k = 1
            result[i][j] = 0
        return result
    def left(self,i,j,result,limit,jump = True):
        k = 0
        for j in range(j,limit - 1,-1):
            if(not jump):
                if(k and self.mat[i][j] != '.'):
                    break
                k = 1
            print(i,j)
            result[i][j] = 0
        return result
    def digRu(self,i,j,result):
        k = 0
        while(1):
            if(k and self.mat[i][j] != '.'):
                break
            k = 1
            result[i][j] = 0
            if(i<0 or j == self.m):
                break
            i -= 1
            j += 1
        return result
    def digLu(self,i,j,result):
        k = 0
        while(1):
            if(k and self.mat[i][j] != '.'):
                break
            k = 1
            result[i][j] = 0
            if(i<0 or j<0):
                break
            i -= 1
            j -= 1
        return result
        
    def digRd(self,i,j,result):
        k = 0
        while(1):
            if(k and self.mat[i][j] != '.'):
                break
            k = 1
            result[i][j] = 0
            if(j == self.m or i == self.n):
                break
            i += 1
            j += 1
        return result

        
    def digLd(self,i,j,result):
        k = 0
        while(1):
            if(k and self.mat[i][j] != '.'):
                break
            k = 1
            result[i][j] = 0
            if(j<0 or i == self.n):
                break
            i += 1
            j -= 1
        return result

    def Rook(self,i,j,result):
        print(result)
        result = self.up(i,j,result,0,False)
        print('up',result)
        result = self.down(i,j,result,self.n-1,False)
        print('down',result)
        result = self.right(i,j,result,self.m-1,False)
        print('right',result)
        result = self.left(i,j,result,0,False)
        print('left',result)
        
        return result

    def Bishop(self,i,j, result):
        result = self.digRu(i,j,result)
        result = self.digLu(i,j,result)
        result = self.digRd(i,j,result)
        result = self.digLd(i,j,result)
        return result
    def Queen(self,i,j, result):
        result = self.Rook(i,j, result)
        result = self.Bishop(i,j, result)
        return result
    def Knight(self,i,j, result):
        result[i][j] = 0
        if(j+2<self.m):
            if(i>0 and self.mat[i-1][j+2] == '.'):
                result[i-1][j+2] = 0
            if(i+1<self.n and self.mat[i+1][j+2] == '.'):
                result[i+1][j+2] = 0
        if(j-2>=0):
            if(i>0 and self.mat[i-1][j-2] == '.'):
                result[i-1][j-2] = 0
            if(i+1<self.n and self.mat[i+1][j-2] == '.'):
                result[i+1][j-2] = 0
        return result


    def Special(self,i,j,result):
        i = min(i,j)
        i = min(i,self.n - i)
        imax = self.n - i

        if(i&1 == 0):
            if(imax & 1 == 0 or i+1 < imax):
                self.down(i,i,result,imax)
                self.up(imax,imax,result,i)
        else:
            self.down(i,i,result,imax)
            self.up(imax,imax,result,i)

        j = min(i,self.m - i)
        jmax = self.m-i

        if(j&1 == 0):
            if(jmax & 1 == 0 or j+1 < jmax):
                result = self.right(j,j,result,imax)
                result = self.left(jmax,jmax,result,j)
        else:
            result = self.right(j,j,result,jmax)
            result = self.left(jmax,jmax,result,j)
        return result
        

    def move(self):
        n = self.n 
        m = self.m
        board = self.mat
        result = self.result
        #print_mat(result)
        for i in range(n):
            for j in range(m):
                if(board[i][j] == '.'):
                    pass
                elif(board[i][j] == 'R'):
                    print("R")
                    print_mat(result)
                    result = self.Rook(i,j, result)
                    print_mat(result)
                elif(board[i][j] == 'B'):
                    print("B")
                    print_mat(result)
                    result = self.Bishop(i,j, result)
                    print_mat(result)
                elif(board[i][j] == 'Q'):
                    print("Q")
                    print_mat(result)
                    result = self.Queen(i,j, result)
                    print_mat(result)
                elif(board[i][j] == 'K'):
                    print("K")
                    print_mat(result)
                    result = self.Knight(i,j,result)
                    print_mat(result)
                elif(board[i][j] == 'S'):
                    print("S")
                    print_mat(result)
                    result = self.Special(i,j,result)
                    print_mat(result)
        s = 0
        for i in range(n):
            s += sum(result[i])
        #print_mat(result)
        return s