def read_columns(number):
    column_data = []
    with open("iris.csv") as iris_file:
        for line in iris_file.readlines()[1:]:
            data = line.strip().split(",")
            column_data.append(data[number])
    return column_data


def get_headers():
    headers = []
    with open("iris.csv") as iris_file:
        data = iris_file.readlines()
        for header in data[0].strip().split(","):
            headers.append(header)
    return headers


# print(get_headers())


def header_picker():
    header = get_headers()
    for counter, index in enumerate(header[:-1]):
        print(f"{counter}- {index}")



