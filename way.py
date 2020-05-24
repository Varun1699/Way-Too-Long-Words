w=int(input())
a=[]
for i in range (0,w):
    p= input()
    a.append(p)
for i in range (0,w):
    r=a[i]
    print(r[0]+str(len(r)-2)+r[-1]) if len(r)>10 else print(r)
