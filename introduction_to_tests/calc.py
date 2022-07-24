""" Example with assert """


def soma(y_v, x_v):
    """
    Soma x e y

    >>> soma(10, 20)
    30

    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError:  the number must be int or float
    """
    assert isinstance(x_v, (int, float)), " the number must be int or float"
    assert isinstance(y_v, (int, float)), " the number must be int or float"
    return x_v + y_v


def subtrai(x_v, y_v):
    """
    >>> subtrai(10,5)
    5

    >>> subtrai('10',5)
    Traceback (most recent call last):
    ...
    AssertionError:  the number must be int or float
    """
    assert isinstance(x_v, (int, float)), " the number must be int or float"
    assert isinstance(y_v, (int, float)), " the number must be int or float"
    return x_v - y_v


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
