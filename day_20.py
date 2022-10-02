from functools import lru_cache, reduce
import math
import time


@lru_cache
def specific_factor(num: int, factor: int) -> set:
    """Return factor pair as set if ::factor is valid factor or ::num"""
    if num % factor == 0:
        return {factor, int(num / factor)}
    return set()


def will_elf_pass_house(house_number: int, elf_number: int) -> bool:
    """Returns True if house is passed by an give elf regardless of whether they deliver there"""
    return house_number <= elf_number * 50


@lru_cache(maxsize=None)
def factorise(num: int):
    """Return set of integer factors of num"""

    factors = [[i, num // i] for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]
    return set(reduce(list.__add__, factors))


def get_number_of_visits_v2(house_number: int) -> int:
    total_visits = 0
    for elf_number in factorise(house_number):
        if will_elf_pass_house(house_number, elf_number):
            total_visits += elf_number
    return total_visits


def get_number_of_visits(house_number: int) -> int:
    """Returns number of presents delivered to a given house"""
    return sum(factorise(house_number))


def part_one(puzzle_input: int) -> int:
    """Solution to part 1"""
    house_number = 1
    gifts_per_elf = 10
    adjusted_puzzle_input = puzzle_input / gifts_per_elf
    number_of_presents = get_number_of_visits(house_number)
    while number_of_presents < adjusted_puzzle_input:
        house_number += 1
        number_of_presents = get_number_of_visits(house_number)
    return house_number


def part_two(puzzle_input) -> int:
    """Solution to part 2"""
    house_number = 1
    gifts_per_elf = 11
    adjusted_puzzle_input = puzzle_input / gifts_per_elf
    number_of_presents = get_number_of_visits_v2(house_number)
    while number_of_presents < adjusted_puzzle_input:
        house_number += 1
        number_of_presents = get_number_of_visits_v2(house_number)
    return house_number


def main():  # pylint:disable=missing-function-docstring

    puzzle_input = 34_000_000

    start_time = time.perf_counter()
    print(part_one(puzzle_input))
    end_time = time.perf_counter()
    print(f"Run time: {end_time-start_time}")

    start_time = time.perf_counter()
    print(part_two(puzzle_input))
    end_time = time.perf_counter()
    print(f"Run time: {end_time-start_time}")


if __name__ == "__main__":
    main()
