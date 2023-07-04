n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

#code to print pyramid pattern using recursion
def pypart(n):
    if n==0:
        return
    else:
        pypart(n-1)
        print("* "*n)
n = 5
pypart(n)


#code to print pyramid pattern using while loop
n=5
i=1;j=0
while(i<=n):
    while(j<=i-1):
        print("* ",end="")
        j+=1
    print("\r")
    j=0;i+=1
