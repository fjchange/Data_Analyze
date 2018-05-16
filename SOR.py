import numpy as np

class SOR :
    def __init__(self,A,b,limit,M,omega):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.n=b.size
        self.M=M
        self.omega=omega

    def cal(self):
        for i in range(self.n):
            if abs(self.A[i][i])<self.limit:
                print("求解失败!")
                return None
            T=self.A[i][i]
            for j in range(self.n):
                self.A[i][j]/=-T
            self.A[i][i]=0
            self.b[i]/=T
        self.Y=np.copy(self.b)
        k=0
        X=np.copy(self.Y)
        while(k<self.M):
            for i in range(self.n):
                self.Y[i]=sum(np.dot(self.A[i],self.Y))+self.b[i]
            if sum(abs(self.Y-X))<self.limit:
                return self.Y
            else:
                k+=1
                X=np.copy(self.Y)
        print("求解失败,循环次数超过给定最大次数!")
        return None