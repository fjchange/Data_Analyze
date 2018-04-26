import numpy as np

class full_var_gauss():
    def __init__(self,A,b,limit):
        self.A=A.astype(float)
        self.b=b.astype(float)
        self.limit=limit
        self.n=b.size

    def  cal(self):
        d=np.zeros(self.n,dtype=int)
        for i in range (self.n):
            d[i]=i
        for k in range(self.n-1):
            k_abs=np.copy(abs(self.A[k:,k:]))
            index=np.where(k_abs==np.max(k_abs))
            T=np.amax(k_abs)
            if T<self.limit:
                print("求解失败！")
                return None
            if index[0]+k!=k:
                temp=np.copy(self.A[k])
                self.A[k]=np.copy(self.A[index[0]+k])
                self.A[index[0]+k]=np.copy(temp)
                tmp=np.copy(self.b[k])
                self.b[k]=np.copy(self.b[index[0]+k])
                self.b[index[0]+k]=np.copy(tmp)
            if index[1]+k!=k:
                temp=np.copy(self.A[:,[k]])
                self.A[:,[k]]=self.A[:,index[1]+k]
                self.A[:,index[1]+k]=temp
                tmp=d[index[1]+k]
                d[index[1]+k]=d[k]
                d[k]=tmp

            for i in range (k+1,self.n):
                T=self.A[i,k]/self.A[k,k]
                self.b[i]=self.b[i]-T*self.b[k]
                self.A[i]=self.A[i]-T*self.A[k]

        self.X=np.zeros_like(self.b,dtype=float)
        self.X[self.n-1]=self.b[self.n-1]/self.A[self.n-1,self.n-1]
        for i in range(self.n-2,-1,-1):
            sum_ax=0
            for j in range(i+1,self.n):
                sum_ax+=self.A[i,j]*self.X[j]
            self.X[i]=(self.b[i]-sum_ax)/self.A[i,i]
        #print(np.dot(self.A,self.X))
        x=np.zeros_like(self.X,dtype=float)
        for i in range(self.n):
            x[i]=self.X[np.where(d==i)]
        self.X=np.copy(x)
        return self.X

A=np.array([[12,-3,3],[0,-1.5,3.5],[0,0,3.66666666666666666667]])
b=np.array([[15],[7.5],[11]])
gauss=full_var_gauss(A,b,1e-4)
print(gauss.cal())
