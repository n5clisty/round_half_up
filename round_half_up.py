
def RHU_int(x):
    from decimal import Decimal, ROUND_HALF_UP
    # This code conducts round half up for a given float value and converts it to an integer.
    return int(Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

def RHU_float(x, rounded):
    from decimal import Decimal, ROUND_HALF_UP
    """
    This code conducts round half up for a given float value at the number of decimals which you defined.
    :param x: the given float
    :param rounded: number of decimals you want to leave
    :return:
    """
    i = 0
    dec = '0.'
    while i < rounded:
        dec = dec + str('0')
        i += 1
    new_x = float(Decimal(str(x)).quantize(Decimal(dec),rounding = ROUND_HALF_UP))
    return new_x