def rev (num):
    r=0
    while num!=0:
        d=num% 10 
        r=r*10+d
        num=num//10
    return r

n=int(input("Enter a number: "))
if n==rev(n):
    print(n,"is a Palindrome number")
else:
    print(n,"is not a Palindrome number")
# Output: Enter a number: 121
        