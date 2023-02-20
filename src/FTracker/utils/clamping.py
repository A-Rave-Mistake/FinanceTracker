def string_to_float(string: str) -> float:
    if isinstance(string, str):
        return float(string.replace(",", "."))
    else:
        raise TypeError("'string_to_float' accepts only 'string' parameter of str type")