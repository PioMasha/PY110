def task() -> list:
    temp_tuple = (0, 36.6, 100)

    return list(map(lambda x: x * 1.8 + 32, temp_tuple))  # TODO  вернуть список температур по Фаренгейту


if __name__ == "__main__":
    print(task())
