# find factors
n=int(input("Enter n: "))
for i in range(1,n+1):#i ->1 to n
    if n%i==0:
        print(i,"is factor of",n)
# Output: 1 is factor of 1533