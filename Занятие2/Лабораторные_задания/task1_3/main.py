def task(numbers: list) -> int:
    return sum(number ** 3 for number in numbers if number < 0)


if __name__ == "__main__":
    list_numbers = [-2, -1, 0, 1, -3, 2, -3]
    print(task(list_numbers))
