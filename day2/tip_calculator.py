print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $ "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15 "))
peoples = int(input("How many people to split the bill? "))

result = round(((bill)+(bill*tip/100))/peoples,2)

print(f"Each person should pay: ${result}")