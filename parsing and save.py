import os
fp_py=[]
fp_py_txt=open('fullpathes_py','w')
for i in os.walk('C:\\Users\idtfs\OneDrive\Рабочий стол\Gleb'):
    for p in i[2]:
##        fp_py.append(p)
##        print (fp_py)
        fp_py.append(os.path.join(i[0],p))
        fp_py_txt.write(os.path.join(i[0],p)+'\n')
fp_py_txt.close()
        
