# write a program to find the largest of three numbers

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number : "))

lg = n1
if n2 > lg:
    lg = n2
if  n3 > lg:
    lg = n3
print(f"largest = {lg}")