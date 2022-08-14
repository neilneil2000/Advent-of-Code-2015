from day_5_input import day_5_input


class Buffer:
    def __init__(self, length: int):
        self.buffer = ["" for _ in range(length)]

    def add_item(self, item):
        self.buffer.pop(0)
        self.buffer.append(item)

    @property
    def pair(self):
        return self.buffer[1] + self.buffer[2]


class StringChecker:
    """Machine to check whether strings are naughty or nice"""

    VOWELS = {"a", "e", "i", "o", "u"}
    NAUGHTY_PAIRS = {"ab", "cd", "pq", "xy"}
    NICE_RETURN = "Nice"
    NAUGHTY_RETURN = "Naughty"

    def __init__(self):
        self.naughty_count = 0
        self.nice_count = 0

    def _is_naughty(self):
        self.naughty_count += 1
        return self.NAUGHTY_RETURN

    def _is_nice(self):
        self.nice_count += 1
        return self.NICE_RETURN

    def check_string(self, string_to_be_checked: str):
        """Given a string it will determine whether it is naughty or nice (Part 1)"""

        double_letter_flag = False
        vowel_count = 0
        previous_letter = ""
        for letter in string_to_be_checked:
            if previous_letter + letter in self.NAUGHTY_PAIRS:
                return self._is_naughty()
            if previous_letter == letter:
                double_letter_flag = True
            if letter in self.VOWELS:
                vowel_count += 1
            previous_letter = letter

        if double_letter_flag and vowel_count >= 3:
            return self._is_nice()
        return self._is_naughty()

    def check_string_new_model(self, string_to_be_checked: str):
        """Given a string it will determine whether it is naughty or nice (Part 2)"""
        pairs = {}
        letters = Buffer(3)
        single_letter_repeat_flag = False
        double_letter_repeat_flag = False

        for position, letter in enumerate(string_to_be_checked):
            letters.add_item(letter)
            if letters.pair in pairs:
                if position > pairs[letters.pair] + 1:
                    double_letter_repeat_flag = True
            else:
                pairs[letters.pair] = position

            if letters.buffer[0] == letters.buffer[2]:
                single_letter_repeat_flag = True

        if single_letter_repeat_flag and double_letter_repeat_flag:
            return self._is_nice()
        return self._is_naughty()

    @property
    def total_checked(self):
        """Total number of strings successfully checked"""
        return self.naughty_count + self.nice_count


def main():
    """Main function"""
    santas_machine = StringChecker()
    strings = day_5_input.splitlines()
    # strings = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
    for string in strings:
        santas_machine.check_string_new_model(string)

    print(f"{santas_machine.total_checked} Strings Checked")
    print(f"Naughty: {santas_machine.naughty_count}")
    print(f"Nice: {santas_machine.nice_count}")


if __name__ == "__main__":
    main()
