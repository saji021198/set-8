r=input()
d=list(r)
z=len(r)
p=""
if (z%2)==0:
    d[int(z/2)]='*'
    d[int(z/2-1)]='*'
else:
    d[int(z/2)]='*'
p=p.join(d)
print(p)
    
