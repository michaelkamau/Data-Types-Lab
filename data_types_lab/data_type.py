
def data_type(value):
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
