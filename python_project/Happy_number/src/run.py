def is_happy_number(n: int):
    """_summary_

    Args:
        n (int): The number that you want to validation is happy or not.

    Returns:
        bool: Retuen boolian value to describe inout
    """
    seen_number = set()
    while (n != 1) and (n not in seen_number):
        seen_number.add(n)
        n = sum([int(n)**2 for n in str(n)])
        
    return n == 1


if __name__ == "__main__":
    assert is_happy_number(13) is True
    assert is_happy_number(45) is not True

