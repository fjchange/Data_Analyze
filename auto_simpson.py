import math

class auto_simpson:
    def __init__(self,a,b,func,limit=0.00001):
         self.a=a
         self.b=b
         self.limit=limit
         self.func=func
         self.s=func(a)+func(b)
         self.T0=0

    def cal(self):
        m=1
        k=1
        #上次的奇数位与偶数位的和
        t0=0
        #这次奇数位的和
        t1=0
        k=0
        while(1):
            n=2*m
            t2 = 0
            h=(self.b-self.a)/n
            if(k==0):
                for i in range(1,m):
                    t1=t1+self.func(self.a+(2*i)*h)
                k+=1
            for i in range(1,m+1):
                t2=t2+self.func(self.a+(2*i-1)*h)
            self.T1=h/3.0*(self.s+4*t2+2*t1)
            if abs(self.T1-self.T0)<3*self.limit:
                return self.T1
            else:
                m=2*m
                t1=t1+t2
                self.T0=self.T1

