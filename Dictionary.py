D1={6:1,9:12,10:20}
D1[4]=40
print(D1)

#modify

D1[9]=100
print(D1)
x=D1.get(90,"Not present")
print(x)

for k,v in D1.items():
    print(k,v)