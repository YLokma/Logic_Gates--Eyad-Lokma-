cie = []
inputs = int(input('How many inputs? \n'))

a=[]
while inputs>=4 and len(a)<8:
    a.append(0)
    
b=[]
while inputs>=3 and len(b)<8:
    b.extend([0,0,0,0,1,1,1,1])
 
c=[]
while inputs>=2 and len(c)<8:
    c.extend([0,0,1,1])
 
d=[]
while inputs>=1 and len(d) < 8:
    d.extend([0,1])

cie.append(a)
cie.append(b)
cie.append(c)
cie.append(d)

print(str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d))
print("####")
