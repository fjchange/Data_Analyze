import math
import numpy as np


def matrix_row_col_stack(a, k):
    return np.column_stack((np.row_stack((a,np.zeros([k-1]))),np.zeros(k)))

class romberg:
    def __init__(self,a,b,func,limit=0.00001):
        self.a=a
        self.b=b
        self.func=func
        self.T=np.zeros([1,1])
        self.T[0, 0]=(b-a)/2.0*(func(a)+func(b))
        self.k=1
        self.limit=limit

    def cal(self):
        while(1):
            self.T=matrix_row_col_stack(self.T,self.k+1)
            S=0
            for i in range(1,(int)(math.pow(2,self.k-1)+1)):
               S+=self.func(self.a+(2*i-1)*(self.b-self.a)/(math.pow(2,self.k)))
            self.T[0,self.k]=0.5*(self.T[0,self.k-1]+(self.b-self.a)/math.pow(2,self.k-1)*S)
            for m in range(1,self.k+1):
                self.T[m,self.k-m]=(pow(4,m)*self.T[m-1,self.k-m+1]-self.T[m-1,self.k-m])/(pow(4,m)-1)
            if abs(self.T[self.k,0]-self.T[self.k-1,0])<self.limit:
                return self.T[self.k,0]
            else:
                self.k+=1
