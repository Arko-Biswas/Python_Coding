

## String ##
print("123" + "345")

## Integer ##
print(123 + 345)

## Type Conversion ##

num_char = len(input("What is your name?"))
#convert num_char into string
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

## Example: Adding the digits of a number ##
number = input("Type a number: ")
num = int(number)
sum = 0
while num > 0:
    sum = sum + (num%10)
    num = num//10
print(f"Sum is: {sum}")

## BMI Calculator ##
height = float(input("Enter your height in meters (m): "))
weight = int(input("Enter your weight in kilos (kg): "))
height_squared = height*height
bmi = round(weight/height_squared)
print(f"Your BMI is: {bmi}")




