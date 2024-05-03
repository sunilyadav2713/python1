import sys
import os
import json
import numpy as np
import matplotlib.pyplot as plt
dirname=sys.argv[1]
files=os.listdir(dirname)
file_path=[]

bar1=[]
for i in files:
    f_p=dirname+"\\"+i
    file_path.append(f_p)
for filename in file_path:
    fiobj=open(filename)
    data=json.load(fiobj)
    fiobj.close()
    rooms_info={'Small':[],'Medium':[],'Large':[],'Phone Booth':[]}
    for i in data:
        for j in i:
            for k,x in j.items():
                if k=='conference-categories-count':
                    for y,z in x.items():
                        if y=="Small":
                            rooms_info['Small'].append(z)
                        elif y=="Medium":
                            rooms_info['Medium'].append(z)
                        elif y=="Large":
                            rooms_info['Large'].append(z)
                        else:
                            rooms_info['Phone Booth'].append(z)
                    
    for p,q in rooms_info.items():
        t=sum(q)/len(q)
        print(p,':',t)
        bar1.append(t)
plt.bar(range(len(bar1)), bar1)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')
plt.show()




        
    
