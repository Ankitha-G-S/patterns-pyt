#left down triangle
n=int(input())
for i in range(0,n,1):
    for j in range(0,n-i,1):
        print("*",end=" ")
    print("\n")
