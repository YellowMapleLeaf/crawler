import doctest

def mysum(x,y):
    """
    :param x:
    :param y:
    :return:sum

    example:
    >>> mysum(1,2)
    3
    """
    return x+y+1

mysum(1,2)

doctest.testmod()




