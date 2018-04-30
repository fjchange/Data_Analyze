import numpy as np

class L_Dt_L():
    def __init__(self,A,b,limit):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.n=b.size

    def cal(self):
        self.U=np.zeros_like(self.A,dtype=float)
        self.d=np.zeros(self.n)
        self.L=np.zeros_like(self.A,dtype=float)
        for k in range(self.n):
            for j in range(k,self.n):
                sum_lu=0.
                for m in range(k):
                    sum_lu+=self.L[k,m]*self.U[m,j]
                self.U[k,j]=self.A[k,j]-sum_lu
                if abs(self.U[k,j])<self.limit:
                    print("求解失败！")
                    return None
            self.d[k]=self.U[k,k]
            for i in range(k+1,self.n):
                self.L[i,k]=self.U[k,i]/self.U[k,k]
            self.Y = np.zeros_like(self.b, dtype=float)
            self.Y[0] = self.b[0] 
            for i in range(1, self.n):
                sum_ly = 0.
                for j in range(i):
                    sum_ly += self.L[i, j] * self.Y[j]
                self.Y[i] = (self.b[i] - sum_ly) / self.L[i, i]