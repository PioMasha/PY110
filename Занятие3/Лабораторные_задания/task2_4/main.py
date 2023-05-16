import json


def task():
    filename = "input.json"
    with open(filename) as f:# TODO считать содержимое JSON файла
        python_object = json.load(f)
    gen_exr = (x["contains_improvement_appeals"] for x in python_object)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
