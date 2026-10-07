import random
import csv
from pathlib import Path

REG_NO = "192565037"
NAME = "Muthupandi C"
SEED = int(REG_NO[-4:])


def generate_dataset(n, seed):
    random.seed(seed)

    records = set()

    while len(records) < n:
        records.add(random.randint(10000000, 99999999))

    records = list(records)

    # Ensure the student's registration number is present.
    records[0] = int(REG_NO)

    # Ensure REG_NO + 1 is a not-found key.
    not_found_key = int(REG_NO) + 1

    if not_found_key in records:
        index = records.index(not_found_key)
        records[index] = 99999999

    return records


def save_dataset(records, filename):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["registration_number"])

        for value in records:
            writer.writerow([value])


if __name__ == "__main__":
    print("DAA ASSIGNMENT 1")
    print("Name:", NAME)
    print("Reg No:", REG_NO)
    print("Personal Seed:", SEED)

    sizes = [1000, 10000, 100000, 1000000]

    for size in sizes:
        records = generate_dataset(size, SEED + size)
        filename = f"data/students_{size}.csv"
        save_dataset(records, filename)
        print(f"Generated {size} records -> {filename}")
