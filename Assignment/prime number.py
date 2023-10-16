#2.Prime Number or not
n=int(input())
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")