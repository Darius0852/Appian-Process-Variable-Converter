import pandas as pd
import ast
import re
from convertOctal import *
from convertNestedArray import *

with open('Example Input - ProcessVariable.txt', 'r') as file:
    inputVar = file.read().replace('\n', '')
print("Your variable is " + inputVar)
print("Lets Convert it!")

octalConvertedInputVar = convert_octals_to_decimals(inputVar)

convertedNestedArray = convert_nested_array(octalConvertedInputVar)



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

print("You're converted process variable: \n")

print(var)






# Example Data: [[id:3, name:"John"]]
# Example Data: [{"A"}, {"B"}]
