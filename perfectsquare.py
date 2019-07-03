import math
r,s=map(int,input().split())
p=r*s
l=math.sqrt(p)
if l==int(l):
    print("yes")
else:
    print("no")


