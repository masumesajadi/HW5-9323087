import math
from time import process_time
import matplotlib.pyplot as plt
import subprocess


class CGaussSolver: 
    
    def __init__(self,pf,a,b,n):
      self.m_Pf=pf
      self.m_A=a
      self.m_B=b
      self.m_N=n
      self.m_Result=0
    
    def legendre(self,m_N, x):
      if m_N == 0:
          return 1
      elif m_N == 1:
          return x
      else:
          return ((2.0 * m_N - 1) / m_N) * x * self.legendre(m_N - 1, x) - ((1.0 * m_N - 1) / m_N) * self.legendre(m_N - 2, x)
    
    
    def dLegendre(self,m_N, x):
        dLegendre=0
        dLegendre = (1.0 * m_N / (x * x - 1)) * ((x * self.legendre(m_N, x)) - self.legendre(m_N - 1, x))
        return dLegendre
    
    
    
    def legendreZeroes(self,m_N,i):
        xnew1, xold1 = 0 , 0
        pi = 3.141592655
        xold1 = math.cos(pi * (i - 1 / 4.0) / (m_N + 1 / 2.0))
        iteration=1 
        while True:
            if iteration != 1:
                xold1 = xnew1
            xnew1 = xold1 - self.legendre(m_N, xold1) / self.dLegendre(m_N, xold1)
            iteration+=1
            if 1 + math.fabs((xnew1 - xold1)) <= 1. :
                break
        return xnew1
    
  
    
    def weight(self,m_N,x):
        weightI=0
        weightI = 2 / ((1 - pow(x, 2)) * pow(self.dLegendre(m_N, x), 2))
        return weightI
    
    
    
    def exec(self):
        integral=0 
        iteration=1 
        iteration+=1
        integral = 0
        #n++;
        for i in range(1,self.m_N+1):
            integral = integral + self.m_Pf(self.legendreZeroes(self.m_N, i)) * self.weight(self.m_N, self.legendreZeroes(self.m_N, i));
            self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral
    
    def getResult(self):
        return self.m_Result
   

    
def aFunction(x):
    xN = 0.5 * x + 0.5
    return (pow(xN, 3) / (xN + 1))*math.cos(pow(xN, 2))




a,b=0,1 #calculate the time of process in python
n=[i for i in range(10,21)]
t=[]
for i in range(11):
    t0=process_time() #start of  process time
    aSolver=CGaussSolver(aFunction,a,b,n[i])
    aSolver.exec()
    t1=process_time()#end of process time
    t.append(t1-t0)#append for ploting
    print("Result of C++ code (n = {} ): {:.20}".format(n,aSolver.getResult()) )
    print( "time:{}".format(t1-t0 ))
    
plt.plot(n,t)



    










