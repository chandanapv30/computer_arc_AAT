# Logical Left and Right Shift on 8-bit Binary Numbers

BITS = 8
MASK = (1 << BITS) - 1


def to_binary8(number):
    """Convert a number to exactly 8-bit binary format."""
    return format(number & MASK, "08b")


def logical_shift(binary, direction, positions):
    print("\nInput binary number:", binary)

    # Convert input to an 8-bit value
    original = int(binary, 2)
    value = original & MASK

    if len(binary) != BITS:
        print("Note: Input is not 8 bits.")
        print("Keeping the least significant 8 bits.")

    print("Original 8-bit number:", to_binary8(value))

    # Perform shifting one position at a time
    for step in range(1, positions + 1):
        if direction == "left":
            value = (value << 1) & MASK
        elif direction == "right":
            value = value >> 1

        print(f"After {direction} shift {step}:",
              to_binary8(value))

    print("Final 8-bit result:", to_binary8(value))


# (a) Logical left shift by 2 positions
print("A) LOGICAL LEFT SHIFT")
logical_shift("1111110110", "left", 2)

# (b) Logical right shift by 2 positions
print("\nB) LOGICAL RIGHT SHIFT")
logical_shift("10010100", "right", 2)