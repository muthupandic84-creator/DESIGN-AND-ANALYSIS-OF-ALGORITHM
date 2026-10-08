import random
import time
import csv
from pathlib import Path

from algo1_linear_search import linear_search
from algo2_binary_search import binary_search
from algo3_hash_table import build_hash_table, hash_search


REG_NO = "192565037"
NAME = "Muthupandi C"

SEED = int(REG_NO[-4:])

SIZES = [
    1000,
    10000,
    100000,
    1000000
]


def generate_dataset(n):

    random.seed(SEED + n)

    records = set()

    while len(records) < n:
        records.add(
            random.randint(10000000, 99999999)
        )

    records = list(records)

    records[0] = int(REG_NO)

    not_found = int(REG_NO) + 1

    if not_found in records:

        index = records.index(not_found)

        records[index] = 99999999

    return records


def run_linear(records, key):

    start = time.perf_counter()

    position, comparisons = linear_search(
        records,
        key
    )

    end = time.perf_counter()

    return position, comparisons, end - start


def run_binary(records, key):

    sorted_records = sorted(records)

    start = time.perf_counter()

    position, comparisons = binary_search(
        sorted_records,
        key,
        0,
        len(sorted_records) - 1
    )

    end = time.perf_counter()

    return position, comparisons, end - start


def run_hash(records, key):

    start_build = time.perf_counter()

    table = build_hash_table(records)

    end_build = time.perf_counter()

    start = time.perf_counter()

    position, operations = hash_search(
        table,
        key
    )

    end = time.perf_counter()

    preprocessing = end_build - start_build

    return position, operations, end - start, preprocessing


if __name__ == "__main__":

    print("=" * 70)
    print("DESIGN AND ANALYSIS OF ALGORITHMS")
    print("ASSIGNMENT 1")
    print("Name:", NAME)
    print("Reg No:", REG_NO)
    print("Personal Seed:", SEED)
    print("=" * 70)

    Path("../results").mkdir(exist_ok=True)

    rows = []

    found_key = int(REG_NO)

    not_found_key = found_key + 1

    for size in SIZES:

        print("\nDataset Size:", f"{size:,}")

        records = generate_dataset(size)

        tests = [
            (found_key, "FOUND"),
            (not_found_key, "NOT FOUND")
        ]

        for key, case in tests:

            position, comparisons, elapsed = run_linear(
                records,
                key
            )

            print(
                f"Linear Search | {case:9} | "
                f"Comparisons: {comparisons:8} | "
                f"Time: {elapsed:.8f}s"
            )

            rows.append([
                "Linear Search",
                size,
                case,
                comparisons,
                elapsed
            ])

            position, comparisons, elapsed = run_binary(
                records,
                key
            )

            print(
                f"Binary Search | {case:9} | "
                f"Comparisons: {comparisons:8} | "
                f"Time: {elapsed:.8f}s"
            )

            rows.append([
                "Binary Search",
                size,
                case,
                comparisons,
                elapsed
            ])

            position, operations, elapsed, preprocessing = run_hash(
                records,
                key
            )

            print(
                f"Hash Table    | {case:9} | "
                f"Operations: {operations:8} | "
                f"Time: {elapsed:.8f}s | "
                f"Preprocess: {preprocessing:.8f}s"
            )

            rows.append([
                "Hash Table",
                size,
                case,
                operations,
                elapsed
            ])

    output = "../results/results.csv"

    with open(output, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Algorithm",
            "Dataset_Size",
            "Case",
            "Comparisons_or_Operations",
            "Time_Seconds"
        ])

        writer.writerows(rows)

    print("\nResults saved to:", output)
