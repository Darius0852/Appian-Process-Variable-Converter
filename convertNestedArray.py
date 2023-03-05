import ast

def convert_nested_array(string_with_nested_array):
    nested_list = ast.literal_eval(string_with_nested_array)
    return nested_list