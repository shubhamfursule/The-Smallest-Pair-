ls=[]
T=int(input())
for a in range(T):
    N=int(input())  
    ls=list(map(int,input().split()))
        
    ls.sort()        
    print(ls[0]+ls[1])