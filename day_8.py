"""Advent of Code 2015 Day 8"""


def read_file(filename: str):
    """Read input file"""
    puzzle_input = []
    with open(filename, "rb") as file_handle:
        for line in file_handle:
            puzzle_input.append(line.strip())

    return puzzle_input


def real_length(byte_string: str) -> int:
    """Returns Real length of string removing escape chars etc"""
    # Find \\
    # Find \"
    # Find \xXX

    ESCAPE_SLASH = 92
    LOWERCASE_X = 120
    DOUBLE_QUOTE = 34

    possible_escape_char_found = False
    hex_char_counter = 0
    reduction_counter = 0

    for letter in byte_string:
        if hex_char_counter:
            hex_char_counter -= 1
            continue
        if possible_escape_char_found:
            possible_escape_char_found = False
            if letter in [ESCAPE_SLASH, DOUBLE_QUOTE]:
                reduction_counter += 1
                continue
            if letter == LOWERCASE_X:
                hex_char_counter += 2
                reduction_counter += 3
                continue
        if letter == ESCAPE_SLASH:
            possible_escape_char_found = True

    return len(byte_string) - reduction_counter - 2


def main():
    """Main Function"""
    puzzle_input = read_file("day_8_input.txt")

    total = 0

    for line in puzzle_input:
        total += len(line) - real_length(line)

    print(total)


if __name__ == "__main__":
    main()
