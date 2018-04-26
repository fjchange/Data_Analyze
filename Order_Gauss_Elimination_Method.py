import numpy as np

class order_gauss():
    def __init__(self,A,b,limit):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.n=b.size

    def  cal(self):
        for k in range(self.n-1):
            if abs(self.A[k,k])<=self.limit:
                print("求解失败！")
                return None
            for i in range (k+1,self.n):
                T=self.A[i,k]/self.A[k,k]
                self.b[i]=self.b[i]-T*self.b[k]
                self.A[i]=self.A[i]-T*self.A[k]
        if abs(self.A[self.n-1,self.n-1])<=self.limit:
            print("求解失败！")
            return None
        self.X=np.zeros_like(self.b,dtype=float)
        self.X[self.n-1]=self.b[self.n-1]/self.A[self.n-1,self.n-1]
        for i in range(self.n-2,-1,-1):
            sum_ax=0
            for j in range(i+1,self.n):
                sum_ax+=self.A[i,j]*self.X[j]
            self.X[i]=(self.b[i]-sum_ax)/self.A[i,i]
        #print(np.dot(self.A,self.X))
        return self.X

A=np.array([[12,-3,3],[-18,3,-1],[1,1,1]])
b=np.array([[15],[-15],[6]])
gauss=order_gauss(A,b,1e-4)
print(gauss.cal())
