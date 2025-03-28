a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

odd_numbers = [i for i in range(a, b+1) if i % 2 != 0]
print("Odd numbers between", a, "and", b, "are:", odd_numbers)
