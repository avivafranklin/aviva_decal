# calculator.py
import aviva_decal.homework7.math_tools as mt

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Choose your operation: ")

if operation == "add":
    result = mt.add(a,b)
elif operation == "subtract":
    result = mt.subtract(a,b)
elif operation == "multiply":
    result = mt.multiply(a,b)
else:
    result = mt.divide(a,b)

print(result)


