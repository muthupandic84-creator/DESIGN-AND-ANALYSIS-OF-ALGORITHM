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

SIZES = [1000, 10000, 100000, 1000000]


def generate_dataset(n):
    random.seed(SEED + n)

    records = set()

    while len(records) < n:
        records.add(random.randint(10000000, 99999999))

    records = list(records)
    records[0] = int(REG_NO)

    not_found = int(REG_NO) + 1

    if not_found in records:
        records[records.index(not_found)] = 99999999

    return records


def run_linear(records, key):
    start = time.perf_counter()
    position, comparisons = linear_search(records, key)
    runtime = time.perf_counter() - start
    return position, comparisons, runtime


def run_binary(records, key):
    start_preprocess = time.perf_counter()
    sorted_records = sorted(records)
    preprocessing = time.perf_counter() - start_preprocess

    start = time.perf_counter()
    position, comparisons = binary_search(
        sorted_records, key, 0, len(sorted_records) - 1
    )
    runtime = time.perf_counter() - start

    return position, comparisons, runtime, preprocessing


def run_hash(records, key):
    start_preprocess = time.perf_counter()
    hash_table = build_hash_table(records)
    preprocessing = time.perf_counter() - start_preprocess

    start = time.perf_counter()
    position, operations = hash_search(hash_table, key)
    runtime = time.perf_counter() - start

    return position, operations, runtime, preprocessing


if __name__ == "__main__":
    print("========================================")
    print("DAA ASSIGNMENT 1 - BENCHMARK")
    print("Name:", NAME)
    print("Reg No:", REG_NO)
    print("Seed:", SEED)
    print("========================================")

    found_key = int(REG_NO)
    not_found_key = int(REG_NO) + 1

    output_file = Path("../results/results.csv")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    rows = []

    for size in SIZES:
        records = generate_dataset(size)

        print(f"\nDataset size: {size}")

        for case_name, key in [
            ("FOUND", found_key),
            ("NOT_FOUND", not_found_key)
        ]:
            pos, comparisons, runtime = run_linear(records, key)

            rows.append([
                size, "Linear Search", case_name,
                runtime, comparisons, 0
            ])

            print(
                f"Linear Search | {case_name} | "
                f"Time={runtime:.8f}s | Comparisons={comparisons}"
            )

            pos, comparisons, runtime, preprocessing = run_binary(
                records, key
            )

            rows.append([
                size, "Binary Search", case_name,
                runtime, comparisons, preprocessing
            ])

            print(
                f"Binary Search | {case_name} | "
                f"Time={runtime:.8f}s | Comparisons={comparisons} | "
                f"Preprocessing={preprocessing:.8f}s"
            )

            pos, operations, runtime, preprocessing = run_hash(
                records, key
            )

            rows.append([
                size, "Hash Table Search", case_name,
                runtime, operations, preprocessing
            ])

            print(
                f"Hash Table Search | {case_name} | "
                f"Time={runtime:.8f}s | Operations={operations} | "
                f"Preprocessing={preprocessing:.8f}s"
            )

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Dataset_Size",
            "Algorithm",
            "Case",
            "Runtime_Seconds",
            "Comparisons",
            "Preprocessing_Seconds"
        ])

        writer.writerows(rows)

    print("\nResults saved to:", output_file)
