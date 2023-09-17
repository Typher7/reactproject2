# Problem1                            40 Points

# Write a program that takes two float numbers as input and prints their sum, addition, multiplication, division.

float_a = float(input("Enter first float: "))
float_b = float(input("Enter second float: "))

sum = float_a + float_b
multiplication = float_a * float_b
norm_div = float_a / float_b
floor_div = float_a // float_b

print("The sum of your inputs are ", sum)
print("The multiplication of your inputs are ", multiplication)
print(" The normal division of your inputs are ", norm_div)
print("The floor division of your inputs are ", floor_div)
