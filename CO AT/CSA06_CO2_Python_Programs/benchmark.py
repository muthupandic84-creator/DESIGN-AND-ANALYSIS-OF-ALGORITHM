"""
Basic comparison-count and timing benchmark.
Run: python benchmark.py

The closest-pair benchmark compares the exact brute-force pair count with
elapsed time for the divide-and-conquer implementation. Timings are local
measurements and will vary by computer.
"""
import random
from time import perf_counter
from sentinelops import closest_logins


def insertion_sort_count(items):
    """Insertion sort that also counts key comparisons."""
    data = list(items)
    comparisons = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if data[j][1] < key[1]:
                data[j + 1] = data[j]
                j -= 1
            else:
                break
        data[j + 1] = key

    return data, comparisons


def make_alert_sets(n, seed=42):
    rng = random.Random(seed)
    random_data = [(f"A{i}", rng.randrange(1, 100000)) for i in range(n)]
    nearly_sorted = sorted(random_data, key=lambda item: item[1], reverse=True)

    # Introduce a small number of adjacent swaps.
    step = max(1, n // 100)
    for i in range(0, n - 1, step):
        nearly_sorted[i], nearly_sorted[i + 1] = (
            nearly_sorted[i + 1], nearly_sorted[i]
        )

    return nearly_sorted, random_data


def benchmark_sorting():
    print("\\nINSERTION SORT COMPARISON COUNTS")
    print("n, input_type, comparisons, elapsed_seconds")
    for n in (1000, 5000, 10000):
        near, random_data = make_alert_sets(n)
        for label, data in (("nearly_sorted", near), ("random", random_data)):
            start = perf_counter()
            _, comparisons = insertion_sort_count(data)
            elapsed = perf_counter() - start
            print(f"{n}, {label}, {comparisons}, {elapsed:.6f}")


def benchmark_closest_pair():
    print("\\nCLOSEST-PAIR COMPARISON")
    print("n, brute_force_pair_checks, divide_conquer_seconds")
    rng = random.Random(123)
    for n in (1000, 4000, 8000):
        points = [(rng.random() * 10000, rng.random() * 10000)
                  for _ in range(n)]
        brute_checks = n * (n - 1) // 2

        start = perf_counter()
        closest_logins(points)
        elapsed = perf_counter() - start

        print(f"{n}, {brute_checks}, {elapsed:.6f}")


if __name__ == "__main__":
    benchmark_sorting()
    benchmark_closest_pair()
