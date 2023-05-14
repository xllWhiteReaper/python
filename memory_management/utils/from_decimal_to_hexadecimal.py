def from_decimal_to_hexadecimal(num_str: str) -> str:
    try:
        return str(hex(int(num_str)))
    except ValueError:
        # Handle the case where the input is not a string representation of an integer
        return num_str
