#1) Read the full file
fo=open("f1.txt")#read mode
print(fo.read())#reading complete file
fo.close()

#2) Read the first 5 characters
fo=open("f1.txt")#read mode
print(fo.read(5))
fo.close()

#3) count the number of vowels in the file
fgit pusho=open("f1.txt")
ch=fo.read(1)
c=0
while ch:#)if ch is existing
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        c+=1
    ch=fo.read(1)
print("Number of vowels:",c)

#5 write in the file f2.txt

fo=open("f2.txt","w")#file will be created automatically
fo.write("Hey")
fo.write("pragyan")
fo.write("Rubaba")
fo.close()

#6) append in the file f2.txt

fo=open("f2.txt","a")# try with 'w' also
fo.write("How are you all?")
fo.close()