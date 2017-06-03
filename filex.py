def fibo(x):
  
    if x == 0 :
        return 0
    elif x == 1 :
        return 1
    else :
        fiboNum = fibo(x-2)+fibo(x-1)
        
        return fiboNum
         
     
n = 10;
for num in range(n):         
    print fibo(num+1)

# def fibonacci(x):
#     fibolist = []
#     fibolist.append(0)
#     fibolist.append(1)
#     
#     for num in range (2,x):
#         fibolist.append(fibolist[num-1] + fibolist[num-2])
#         
#     print fibolist 
#     
# fibonacci(11)