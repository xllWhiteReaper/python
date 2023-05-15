def from_decimal_to_hexadecimal(num_str: str) -> str:
    try:
        return str(hex(int(num_str)))
    except ValueError:
        return num_str
