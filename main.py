import pandas as pd
# import ast

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



var = var.replace("[", "{")
var = var.replace("]", "}")
var = var.replace("=", ":")
var = var.replace("=,", ":null,")
var = var.replace("=]", ":null]")
var = var.replace(":,", ":null,")
var = var.replace(":]", ":}")

print("You're converted process variable: \n")

print(var)






# Example Data: [[id:3, name:"John"]]
# Example Data: [{"A"}, {"B"}]
