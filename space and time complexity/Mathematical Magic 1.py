n=int(input("Enter the number: ")) #153
m=n #153
sum=0
while n!=0:
    r=n%10 #3, 5, 1
    sum=sum + r*r*r #0 + 27= 27, 27+125=152, 152+1=153
    n=n//10 # 15, 1, 0
if sum==m:
    print(m,"Armstrong number")
else:
    print(m,"Not an Armstrong number")
# Output: 153 Armstrong number
