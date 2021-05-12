
class Boundaries:
    left = 12.09077
    right = 18.8583483
    up = 51.0517297
    down = 48.5493161

    int_conv_factor = 10**7


Boundaries.left_int = int(Boundaries.left * Boundaries.int_conv_factor)
Boundaries.right_int = int(Boundaries.right * Boundaries.int_conv_factor)
Boundaries.up_int = int(Boundaries.up * Boundaries.int_conv_factor)
Boundaries.down_int = int(Boundaries.down * Boundaries.int_conv_factor)
