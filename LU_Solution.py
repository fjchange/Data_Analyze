import numpy as np

class LU:
    def __init__(self,A,b,limit):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.U=np.zeros_like(A,dtype=float)
        self.n=A.shape[0]
        self.L=np.eye(self.n,dtype=float)

    def cal(self):
        for k in range(self.n):
            for j in range(k,self.n):
                sum_lu=0
                for m in range(k):
                    sum_lu+=self.L[k,m]*self.U[m,j]
                self.U[k,j]=self.A[k,j] - sum_lu
                if k==j and abs(self.U[k,j])<self.limit:
                    print("求解失败！")
                    return None
                else:
                    for i in range(k+1,self.n):
                        sum_lu=0
                        for m in range(k):
                            sum_lu+=self.L[i,m]*self.U[m,k]
                        self.L[i,k]=(self.A[i,k]-sum_lu)/self.U[k,k]
        check=np.dot(self.L,self.U)
        self.Y=np.zeros_like(self.b,dtype=float)
        self.Y[0][0]=self.b[0][0]
        self.U_inverse=np.linalg.inv(self.U)
        self.L_inverse=np.linalg.inv(self.L)
        for i in range(1,self.n):
            sum_ly=0
            for j in range(i):
                sum_ly+=self.L[i,j]*self.Y[j]
            self.Y[i][0]=self.b[i][0]-sum_ly
        self.X=np.zeros_like(self.Y)
        self.X[-1][0]=self.Y[-1][0]/self.U[-1,-1]
        for i in range(self.n-1,-1,-1):
            sum_ux=0
            for j in range(i+1,self.n):
                sum_ux+=self.U[i,j]*self.X[j][0]
            self.X[i][0]=(self.Y[i][0]-sum_ux)/self.U[i,i]
        return self.X

A=np.array([[12,-3,3],[0,-1.5,3.5],[0,0,3.66666666666666666667]])
b=np.array([[15],[7.5],[11]])
lu=LU(A,b,1e-4)
print(lu.cal())