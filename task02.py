from pathlib import Path

file = Path("data_cats.txt")
path = Path.resolve(file)


def get_cats_info(path):
    """
    Reads cat information from a file and returns it as a list of dictionaries.

    Args:
        path (Path): The path to the file containing cat information.

    Returns:
        list: A list of dictionaries with keys 'id', 'name', and 'age'.
              Returns (0, 0) if the file is not found or an error occurs.
    """
    try:
        with open(path, 'r', encoding='utf-8') as data:
            clianed_data = [el.strip() for el in data.readlines() if el.strip()]
            result = []
        for row in clianed_data:
            id_, name, age = row.split(',')
            result.append({'id': id_, 'name': name, 'age': int(age)})
        return result

    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return (0, 0)
    except Exception as e:
        print(f"Error:{e}")
        return (0, 0)


cats_info = get_cats_info(path)
print(cats_info)