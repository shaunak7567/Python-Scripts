import subprocess,os
#cmd="cd /sc/ && du -hs * | sort -n -r | grep G | awk {'print $1 \"    \" $2'}"

cmd1="cd /sc/ && du -hs * | sort -n -r | grep G | awk {'print $1'}"
cmd2="cd /sc/ && du -hs * | sort -n -r | grep G | awk {'print $2'}"
list1=[]
file_sizes={}
print(cmd1) 
ps1=subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
ps2=subprocess.Popen(cmd2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output1=ps1.communicate()[0]
output2=ps2.communicate()[0]
#print (output)
#print (output2)
output1=output1.split("\n")
output2=output2.split("\n")
print(output1)
print(output2)
limit='2G'
diction=dict(zip(output1,output2))
for k in diction.keys():
    if len(diction[k])<1:
        del diction[k]

for l in diction.values():
    print(l)
    path="/sc/"+l 
    if os.path.isdir(path):  
        print("\nIt is a directory")  
    elif os.path.isfile(path):  
        print("\nIt is a normal file")  
    else:  
        print("It is a special file (socket, FIFO, device file)" ) 
print(diction)
