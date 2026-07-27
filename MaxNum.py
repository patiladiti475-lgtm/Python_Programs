Maximum = lambda no1, no2: no1 if no1 > no2 else no2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Maximum number is:", Maximum(num1, num2))