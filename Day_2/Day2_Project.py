print("Welcome to Tip Calculator!!")
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_ppl = int(input("How many people should split the bill? "))
each_person_bill = round(((total_bill + (total_bill * tip_percentage)/100)/num_of_ppl), 2)
print(f"Each person should pay: ${each_person_bill}")






