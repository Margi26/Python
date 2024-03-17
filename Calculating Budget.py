
# Budget Analysis
print("A program for calculating Budget")
# asks the user to enter the amount that he or she has budgeted for a month
budget = int(input("Enter the budget of the month: "))
extra = 'y'  # Variable to control the loop

total = 0.0

# Process to calculate total expenses for the month
while extra == 'y' or extra == 'Y':
    # Get the expenses
    expenses = float(input("Enter the expenses for the month: "))
    total += expenses
    # Do this again ?
    extra = input("Do you have another expenses for the month? " +
                    "(Enter y for yes): ")

# Loop for Getting Output

if total > budget:
    print(\n"You are ${total - budget} over the budget ")
elif total == budget:
    print(\n"Your budget is enough for expenses!")
else:
    print(\n"You are ${total - budget} under the budget ")

print(\n"Total: ${total}")








#Sum of Numbers

print("A program to display sum of Positive Numbers")

sum = 0 
num = 0

while num >= 0:
	num = int(input("Enter positive number to add or negative to end"))
	if num >= 0:
		sum += num 
print("Sum of enterd Positive numbers is = ", sum)

# Ocean Levels

print("A program to calculate Ocean level for next 25 years")
# Rise per year in millimeters

rise_per_year = 1.6 
num_years = 25

for year in range(1, num_years+1):
    rise_this_year = rise_per_year * year
    print(f"Year {year}: {rise_this_year} millimeters")
