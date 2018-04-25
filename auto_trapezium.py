import math
class auto_trap:
    def __init__(self,a,b,func,limit=0.00001):
         self.a=a
         self.b=b
         self.h=(b-a)/2.0
         self.limit=limit
         self.func=func
         self.T1=(func(a)+func(b))*self.h

    def cal(self):
        n=2
        while (1):
            self.T0=self.T1
            S=0
            for i in range(1,n):
                t=self.a+(2*i-1)*self.h/n
                S=S+self.func(t)
            self.T1=self.T0/2.0+S*self.h/n
            if abs(self.T1-self.T0)<3*self.limit:
                return self.T1
            else:n=2*n

