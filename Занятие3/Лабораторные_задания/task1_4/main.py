INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as input_f:  # TODO перезаписать содержимое одного файла в другой
        with open(OUTPUT_FILE) as output_f:
            map(lambda hight_registr: output_f.write(hight_registr.upper()), input_f)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
