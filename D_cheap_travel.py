import math

n ,m,a,b=map(int,input().split())#4
op1=n*a #2
op2=((n//m)*b) + ((n%m)*a)#6
op3= math.ceil(n/m)*b#4

ans=min(op1,op2,op3) #4
print(ans)#1
