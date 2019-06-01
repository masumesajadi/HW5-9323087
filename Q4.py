import random as r
import math as m

def IsInCircle(x,y):
    if m.sqrt(x**2 + y**2) < 1.0:
        print('in')
    else:
        print('out')
        
def find(n):
    inside = 0
    total = 1
    error=1
    jam=0
    final=1
    j=1
    while j<n:
        while abs(error)>0.001:
            for i in range(0, total):
                x = r.random()
                y = r.random()
                if m.sqrt(x**2 + y**2) < 1.0:
                    inside += 1
            
            pi = (float(inside) / total) * 4
            error= pi-3.14159
            print( "total = %-8d   PI = %8.6f   error = %+9.6f" % (total, pi ,error))
 
            if abs(error)<0.001:
                print('well .error<0.001 ')
                print('min point requre is :',total)
            else:
                total=total+1
                inside=0
        jam=jam+total
        j+=1
    final=jam/n
    print('avrage point' , final)    

