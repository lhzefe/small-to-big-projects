print("TIP CALCULATOR")
bill_value = float(input("What was the value of total bill? "))
percentage = int(input("How much of percentage you would like to give? 10, 12 or 15? "))
number_person = int(input("How many people to split the bill? "))

final_value = bill_value + (bill_value * (percentage / 100))
value_person = final_value / number_person

print(f"Each person should pay: ${value_person}")
