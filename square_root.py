import numpy as np
import math

class square_root():
    def __init__(self,A,b,limit):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.n=b.size

    def cal(self):
        self.L=np.zeros_like(self.A,dtype=float)
        for k in range (self.n):
            sum_l_square=0.
            for m in range(k):
                sum_l_square+=self.L[k,m]**2
            s=self.A[k,k]-sum_l_square
            if s<self.limit:
                print("求解失败！")
                return None
            self.L[k,k]=math.pow(s,0.5)
            for i in range(k+1,self.n):
                sum_l=0.
                for m in range(k):
                    sum_l+=self.L[i,m]*self.L[k,m]
                self.L[i,k]=(self.A[i,k]-sum_l)/self.L[k,k]
        self.Y=np.zeros_like(self.b,dtype=float)
        self .Y[0]=self.b[0]/self.L[0,0]
        for i in range(1,self.n):
            sum_ly=0.
            for j in range(i):
                sum_ly+=self.L[i,j]*self.Y[j]
            self.Y[i]=(self.b[i]-sum_ly)/self.L[i,i]
        self.X=np.zeros_like(self.b,dtype=float)
        self.X[-1]=self.Y[-1]/self.L[-1,-1]
        for i in range(self.n-2,-1,-1):
            sum_lx=0.
            for j in range(i+1,self.n):
                sum_lx+=self.L[j,i]*self.X[j]
            self.X[i]=(self.Y[i]-sum_lx)/self.L[i,i]
        return self.X

A=np.array([[3,2,1],[2,2,0],[1,0,3]])
b=np.array([[5],[3],[4]])
s_r=square_root(A,b,1e-4)
print(s_r.cal())

