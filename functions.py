def convert_number(value):
    try:
        int(value)
        return str(int(value))
    except ValueError:
        return str(value)