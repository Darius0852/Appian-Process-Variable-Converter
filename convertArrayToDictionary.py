def convert_string_to_list_of_dicts(string_with_comma_separated_pairs):
    # Split the string by the comma and create a list
    list_of_strings = string_with_comma_separated_pairs.split(",")

    # Create a list of dictionaries
    list_of_dicts = []

    # Create a dictionary of key-value pairs and append it to the list
    for i in range(0, len(list_of_strings), 9):
        sub_dict = {}
        for j in range(i, i+9):
            key_val_pair = list_of_strings[j].split("=")
            sub_dict[key_val_pair[0]] = key_val_pair[1]
        list_of_dicts.append(sub_dict)

    return list_of_dicts