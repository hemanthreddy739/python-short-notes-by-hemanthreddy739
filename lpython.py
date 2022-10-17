'''n=input()
ln=len(n)
ds=""+n[0]
f=0
if (ln >=1 and ln <=100):
    for i in range(1,ln):
        if(ds[-1]!=n[i]):
            
            ds=ds+n[i]
            
        else:
            f=1
            
    
   '''
'''
tn=int(input())
nums=list(map(int,input().strip().split()))[:tn]
nq=int(input())
qs=list(map(int,input().strip().split()))[:nq]
rs=[]
for i in qs:
    c=0
    for j in nums:
        if i==j:
            c+=1
    rs.append(c)

for s in rs:
    if s==0:
        print("Not Present")
    else:
        print(s)
        
        
        '''

'''
a=bin(15)
#print(type(a))
b=a[2:]
print(b)
s=0
for i in b:
    s+=int(i)
print(s)
'''
'''
n=int(input())
nl=list(map(int,input().strip().split()))[:n]
bl=[]
bnl=[]
inl=[]

for i in nl:
    a=bin(i)
    bl.append(a[2:])
for i in bl:
    s=0
    for k in i:
        s+=int(k)
    bnl.append(s)
snl=sorted(bnl,reverse=True)
print(snl)
for i in snl:
    inl.append(bnl.index(i))
print(inl)    

#for i in inl:
    
    #print(nl[i],end=" ")



'''



n=input()
k=len(n)
kn=0
if(k>=1 and k<=100):
    for i in range(k):                           
        if(n[i]==n[(-1-i)]):
            kn+=i
        else:
            break
print(n[kn:-kn])
            
        
































 





















    
