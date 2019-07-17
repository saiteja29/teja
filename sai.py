x,y=input().split()
z=abs(len(y)-len(x))
for i in range(len(x)):
    if(len(y)==1 and y[i] in u):
        break
    if(x[i]!=y[i]):
        z=z+1
print(z)
