# Signed Binary Arithmetic using 16-bit 2's Complement

BITS_8 = 8
BITS_16 = 16


def to_binary(number, bits):
    """Convert a signed integer to its two's complement binary format."""
    mask = (1 << bits) - 1
    return format(number & mask, f"0{bits}b")


def from_binary(binary_value, bits):
    """Convert a two's complement bit pattern to a signed integer."""
    sign_bit = 1 << (bits - 1)

    if binary_value & sign_bit:
        return binary_value - (1 << bits)

    return binary_value


def check_overflow(a, b, result):
    """Check signed arithmetic overflow."""
    return (
        (a >= 0 and b >= 0 and result < 0)
        or
        (a < 0 and b < 0 and result >= 0)
    )


def perform_addition(a, b):
    print("\nExpression: ({}) + ({:+d})".format(a, b))
    print("-" * 55)

    # Display operands in 8-bit two's complement
    print("8-bit operands:")
    print(f"A = {to_binary(a, BITS_8)} ({a})")
    print(f"B = {to_binary(b, BITS_8)} ({b})")

    # Convert operands to 16-bit two's complement
    a16 = a & ((1 << BITS_16) - 1)
    b16 = b & ((1 << BITS_16) - 1)

    # Perform 16-bit binary addition
    sum16 = (a16 + b16) & ((1 << BITS_16) - 1)

    # Convert the resulting bit pattern to a signed decimal value
    result16 = from_binary(sum16, BITS_16)

    print("\n16-bit binary addition:")
    print(f"  {to_binary(a, BITS_16)}")
    print(f"+ {to_binary(b, BITS_16)}")
    print("-" * 19)
    print(f"  {to_binary(sum16, BITS_16)}")

    print("\nFinal 16-bit result:")
    print(f"Binary : {to_binary(result16, BITS_16)}")
    print(f"Decimal: {result16}")

    overflow16 = check_overflow(a, b, result16)
    print("16-bit signed overflow:",
          "YES" if overflow16 else "NO")

    # Also verify the result in 8-bit arithmetic
    a8 = a & ((1 << BITS_8) - 1)
    b8 = b & ((1 << BITS_8) - 1)

    sum8 = (a8 + b8) & ((1 << BITS_8) - 1)
    result8 = from_binary(sum8, BITS_8)

    carry_out8 = (a8 + b8) >> BITS_8
    overflow8 = check_overflow(a, b, result8)

    print("\n8-bit verification:")
    print(f"Result binary : {to_binary(result8, BITS_8)}")
    print(f"Result decimal: {result8}")
    print(f"Carry-out     : {carry_out8}")
    print("8-bit signed overflow:",
          "YES" if overflow8 else "NO")


# Test the given expressions
perform_addition(24, 17)
perform_addition(-25, -18)