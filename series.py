def fibonacci(n):
    """
    Returns the nth element of the fibonacci series.
    :param n:
    :return fibonacci_series[n]:
    """
    seq = [0, 1]
    try:
        if n < 2:
            return seq[n]
        for i in range(n):
            next_num = seq[-1] + seq[-2]
            seq.append(next_num)

    except TypeError:
        print('This function only accepts integers.')
        return None

    else:
        return seq[n]


def lucas(n):
    """
    Returns the nth element of the lucas series.
    :param n:
    :return fibonacci_series[n]:
    """
    seq = [2, 1]

    try:
        if n < 2:
            return seq[n]
        for i in range(n):
            next_num = seq[-1] + seq[-2]
            seq.append(next_num)

    except TypeError:
        print('This function only accepts integers.')
        return None

    else:
        return seq[n]


def series(n, seq_0=0, seq_1=1):
    """
    Returns the nth element of a custom series. By default, it uses the fibonacci series.
    :param seq_1:
    :param seq_0:
    :param n:
    :return fibonacci_series[n]:
    """
    seq = [seq_0, seq_1]

    try:
        if n < 2:
            return seq[n]
        for i in range(n):
            next_num = seq[-1] + seq[-2]
            seq.append(next_num)

    except TypeError:
        print('This function only accepts integers.')
        return None

    else:
        return seq[n]