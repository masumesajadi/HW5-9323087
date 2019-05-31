
#part 2 of qustion 6:
import subprocess
from time import process_time#calculate the time of process in c++
import matplotlib.pyplot as plt


n=[i for i in range(10,21)]
t=[]
for i in range(11): 
    t0=process_time() #start of process time
    subprocess.call(["Project2.exe",str(n[i])])#this code used for run c++ code by python
    t1=process_time() #end of process time
    t.append(t1-t0)
    print( "time for n={} is:{}".format(n[i],t1-t0) )
    
plt.plot(n,t)
    