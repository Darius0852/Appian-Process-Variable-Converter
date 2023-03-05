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

print(convertedNestedArray)