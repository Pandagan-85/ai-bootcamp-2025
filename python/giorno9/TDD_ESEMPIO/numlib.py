def split_text_num(text):
    """Split the given text into two integers"""
    a, b = text.split()
    return (int(a), int(b))


def abs_diff(a, b):
    """Return the absolute value of the different between two numbers"""
    return abs(a - b)
