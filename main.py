import ast

var = input("Enter you're process variable: ")
print("Your variable is " + var)
print("Lets Convert it!")

# Convert Process Variable

my_list = ast.literal_eval(var)
print(my_list)
