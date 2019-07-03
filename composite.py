r=int(input())
for i in range(2,r):
    d=r%i
    if d==0:
        print("yes")
        break
else:
    print("no")
