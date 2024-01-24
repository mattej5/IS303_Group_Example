# Vin Jones

# Description: Prompt user for information to calculate BMI, then displays name, BMI, and weight category.

# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# Prompt user for info, format strings for readability in the Python Shell
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
iFeetHeight = int(input("Enter your height in feet (whole number): "))
iInchHeight = int(input("Enter your remaining height in inches (whole number): "))
iWeight = int(input("Enter your weight in lbs (whole number): "))

# Calculate BMI algorithm after finding total height, then round to 2 decimals
iTotalHeight = (iFeetHeight * 12) + iInchHeight
fBMI = (iWeight / (iTotalHeight ** 2)) * 703
fBMI = round(fBMI, 2)

# Use comparisons to find BMI category
if (fBMI < 18.5) :
    sCategory = "Underweight"
elif (fBMI < 25 and fBMI >= 18.5) :
    sCategory = "Normal Weight"
elif (fBMI < 30 and fBMI >= 25) :
    sCategory = "Overweight"
else:
    sCategory = "Obese"

# Print the final statement
print(f"{sFirstName} {sLastName} has a BMI of {fBMI}. The associated category is: {sCategory}")