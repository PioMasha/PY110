import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda x: x["length"])  # TODO отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    new_filename = "output_json"  # TODO дополнительно записать отсортированный список в JSON файл
    with open(new_filename, "w") as file:
        json.dump(data, file, indent=4)
