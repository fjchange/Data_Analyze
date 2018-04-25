import numpy as np

class LU_col:
    def __init__(self,A,b,limit):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.U=np.zeros_like(A,dtype=float)
        self.n=A.shape[0]
        self.L=np.zeros((self.n,self.n),dtype=float)

    def cal(self):
        for k in range(self.n):
            S=np.zeros(self.n,dtype=float)
            for i in range(k,self.n):
                sum_lu = 0
                for m in range(k):
                    sum_lu += self.L[i, m] * self.U[m, k]
                S[i]=abs(self.A[i,k]-sum_lu)
            index=np.argmax(S)
            if(np.max(S)<self.limit):
                print("求解失败！")
                return None
            else:
                temp=np.copy(self.A[index])
                self.A[index]=np.copy(self.A[k])
                self.A[k]=np.copy(temp)
                tmp=np.copy(self.b[index])
                self.b[index]=np.copy(self.b[k])
                self.b[k]=np.copy(tmp)
                temp=np.copy(self.L[index])
                self.L[index]=np.copy(self.L[k])
                self.L[k]=np.copy(temp)
                temp=np.copy(self.U[index])
                self.U[index]=np.copy(self.U[k])
                self.U[k]=np.copy(temp)


                for j in range(k,self.n):
                    sum_lu=0
                    for m in range(k):
                        sum_lu+=self.L[k,m]*self.U[m,j]
                    self.U[k,j]=self.A[k,j] - sum_lu

                for i in range(k + 1, self.n):
                    sum_lu = 0
                    for m in range(k):
                        sum_lu += self.L[i, m] * self.U[m, k]
                    self.L[i, k] = (self.A[i, k] - sum_lu) / self.U[k, k]
        self.L=self.L+np.eye(self.n,dtype=float)
        check=np.dot(self.L,self.U)
        Y=np.zeros_like(self.b,dtype=float)
        Y[0][0]=self.b[0][0]
        for i in range(1,self.n):
            sum_ly=0
            for j in range(i):
                sum_ly+=self.L[i,j]*Y[j]
            Y[i][0]=self.b[i][0]-sum_ly
        self.X=np.zeros_like(Y)
        self.X[-1][0]=Y[-1][0]/self.U[-1,-1]
        for i in range(self.n-1,-1,-1):
            sum_ux=0
            for j in range(i+1,self.n):
                sum_ux+=self.U[i,j]*self.X[j][0]
            self.X[i][0]=(Y[i][0]-sum_ux)/self.U[i,i]
        return self.X

A=np.array([[1,2,1],[2,2,3],[-1,-3,0]])
b=np.array([[0],[3],[2]])
lu=LU_col(A,b,1e-4)
print(lu.cal())