#
fo=open("f1.txt")
L=fo.read()
print(L)
L=fo.read(5)
print(L)
L=fo.readline()
print(L)
fo.close()
fo=open("f1.txt")
for i in range(3):
    L=fo.readline()
    print(L)

    fo=open("f1.txt")
    L=fo.readline()
    c=0
    while L:
        c+=1
        if c%2==0:
            print(L.rstrip())
        L=fo.readline()

    
fr=open("f1.txt")
fw=open("f11.txt","w")
L=fr.readline()

#5)
c=0
while L:
    c+=1
    if c%2!=0:
        fw.write(L)
    L=fr.readline()
fr.close()
fw.close()

#6)
fr=open("f1.txt")
fw=open("f11.txt","w")
L=fr.readline()

while L:
    if L.startswith("t"):
        fw.write(L)
    L=fr.readline()
fr.close()
fw.close()

      
