#7 count the number of the words 
fo=open("f1.txt")
L=fo.readline()
# line is read with /newline character/enter key) at the end
c=0
while L:
    c=c+1
    Li=L.split()#[hello, how, are, you?]
    print("Line",c,"The number of words = ",len(Li))
    L=fo.readline()

    #Acp) take only t

#8) diplay the longest word from each line 
fo=open("f1.txt")
L=fo.readline()
# line is read with /newline char/enter key) at the end

while L:
    Li=L.split()#[hello, how, are, you?]
    x=0 #to store the length of word
    for w in Li:
       y=len(w)
       if y>x:
            x=y #5, 3, 7
            w1=w
    print("Longest word in",L,"is",w1, "with",x,"characters\n\n")
    L=fo.readline()

#9) delete a file and the folder
import os
if os.path.exists("f11.txt"):
    os.remove("f11.txt")
else:
    print("File does not exist")
os.rmdir("Demo")

#10) remove duplicate lines from file
fo=open("f2.txt")
fi=open("f3.txt","w")
L=fo.readline()
L1=[]
while L:
    if L not in L1:
        L1.append(L)
        fi.write(L)
    L=fo.readline()
fi.writelines(L1)
fo.close()
fi.close()
import os
os.remove("f2.txt")
os.rename("f3.txt","f2.txt")
#acp) take only words that contains "the" in to another file


