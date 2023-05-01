from itertools import count


def task():
    counter = count(100, 10)
    for _ in range(10):
        elements = next(counter)
        print(elements)
    # TODO распечатать с столбик первые 10 чисел бесконечного итератора


if __name__ == "__main__":
    task()
