from hashlib import md5


def main():
    """Main function"""
    puzzle_input = b"ckczppom"
    suffix_number = 0

    print(f"Finding hash for {puzzle_input}")

    while True:
        suffix_number += 1
        hash_input = puzzle_input + bytes(str(suffix_number), "UTF-8")
        hash_output = md5(hash_input)
        if hash_output.hexdigest()[:5] == "00000":
            break

    print(f"Matching Hash Found for {puzzle_input}")
    print(
        f"{suffix_number} is first number to result in 5 digest 0 prefix in hash digest"
    )
    print(f"Hash Output is: {hash_output.hexdigest()}")

    while True:
        suffix_number += 1
        hash_input = puzzle_input + bytes(str(suffix_number), "UTF-8")
        hash_output = md5(hash_input)
        if hash_output.hexdigest()[:6] == "000000":
            break

    print(f"Matching Hash Found for {puzzle_input}")
    print(
        f"{suffix_number} is first number to result in 6 digest 0 prefix in hash digest"
    )
    print(f"Hash Output is: {hash_output.hexdigest()}")


if __name__ == "__main__":
    main()
