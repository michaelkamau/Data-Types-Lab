
def data_type(value):
    if isinstance(value, str):
        return len(value)
    elif isinstance(value, type(None)):
        return 'no value'
