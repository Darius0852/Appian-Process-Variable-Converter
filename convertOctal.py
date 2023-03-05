import re

def convert_octals_to_decimals(string_with_octals):
    pattern = r'0o[0-7]+'

    def convert_octal(match):
        return str(int(match.group(0), 8))

    decimal_string = re.sub(pattern, convert_octal, string_with_octals)
    return decimal_string