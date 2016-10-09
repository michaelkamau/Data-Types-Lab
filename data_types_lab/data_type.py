def data_type(value):
    """
    This function does comparisons on the parameter and returns an output according to the type of the argument

    The following rules are used:
        - For strings, return its length.
        - For None return string 'no value'
        - For booleans return the boolean passed
        - For integers return a string showing how it compares to 100
        - For lists return the 3rd item, or None if it doesn't exist

    :param: value

    :return: outcome depending on the type of the argument passed
    """
    if isinstance(value, str):
        return len(value)
    elif isinstance(value, type(None)):
        return 'no value'
    elif isinstance(value, bool):
        return value
    elif isinstance(value, int):
        if value == 100:
            return 'equal to 100'
        elif value < 100:
            return 'less than 100'
        else:
            return 'more than 100'
    elif isinstance(value, list):
        if len(value) < 3:
            return None
        else:
            return value[2]
