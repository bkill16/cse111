import random


def main():
    numbers = [16.2, 75.1, 52.3]

    print("Initial numbers:", numbers)

    append_random_numbers(numbers)

    print("After appending one number:", numbers)

    append_random_numbers(numbers, 3)

    print("After appending three more numbers:", numbers)


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)


if __name__ == "__main__":
    main()
