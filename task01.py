from pathlib import Path

file = Path("developers_salary.txt")
path = Path.resolve(file)

def total_salary(path):
    """
    Calculate the total and average salary from a file.

    Args:
        path (Path): The path to the file containing salary data.

    Returns:
        tuple: A tuple containing the total salary and the average salary.
    """
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            clianed_lines = [el.strip() for el in fh.readlines() if el.strip()]
            total = 0
            count = 0
            for line in clianed_lines:
                try:
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Error: Invalid line '{line}'")
            if count == 0:
                return (0, 0)
        average = total / count
        return total, average
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return (0,0)
    except Exception as e:
        print(f"Error: {e}")
        return (0, 0)

total, average = total_salary(path)
print(f"Total salary amount: {total}, Average salary: {int(average)}")


