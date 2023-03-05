import pandas as pd
import ast
import re

# var = input("Enter you're process variable: ")

with open('Example Input - ProcessVariable.txt', 'r') as file:
    var = file.read().replace('\n', '')
print("Your variable is " + var)
print("Lets Convert it!")

# Convert Process Variable

# my_list = ast.literal_eval(var)
# df = pd.json_normalize(var)
# print(df)

# SPLIT EVERYTHING
# ******************************************

# splitVar = var.split(']')

# for x in splitVar:
#     print("EQUALS " + x)

# print("SplitVar is " + splitVar)

# ******************************************

# var = var.replace("[", "{")
# var = var.replace("]", "}")
# var = var.replace("=", ":")
# var = var.replace("=,", ":null,")
# var = var.replace("=]", ":null]")
# var = var.replace(":}", ":null}")
# var = var.replace(":,", ":null,")

# print("You're variable has been converted: \n")

# print(var)

# Regular expression to find octal numbers with 0o prefix
pattern = r'0o[0-7]+'

# Function to convert octal numbers to decimal
def convert_octal(match):
    return str(int(match.group(0), 8))

# Replace octal numbers with decimal equivalent
decimal_string = re.sub(pattern, convert_octal, var)

print(decimal_string)

#Convert string to list:
nested_list = ast.literal_eval(decimal_string)

print("You're converted process variable: \n")

print(nested_list)



# Example Data: [[id:3, name:"John"]]
# Example Data: [{"A"}, {"B"}]
