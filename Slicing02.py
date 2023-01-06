def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s) > 4:
        return s[-4:-1] + s[-1]
    else:
        return s

print(main('hello'))

