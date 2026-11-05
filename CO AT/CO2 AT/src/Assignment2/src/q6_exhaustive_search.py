# DAA Assignment 2
# Q6: Exhaustive Search and Combinatorial Growth
# Problem: Humanitarian Airlift Planning

import time


def exhaustive_search(packages, capacity):
    n = len(packages)

    best_value = 0
    best_weight = 0
    best_combination = []

    candidates_examined = 0
    feasible_solutions = 0

    for mask in range(1 << n):
        candidates_examined += 1

        total_weight = 0
        total_value = 0
        selected = []

        for i in range(n):
            if mask & (1 << i):
                package_id, weight, value = packages[i]

                total_weight += weight
                total_value += value
                selected.append(package_id)

        if total_weight <= capacity:
            feasible_solutions += 1

            if total_value > best_value:
                best_value = total_value
                best_weight = total_weight
                best_combination = selected

    return (
        best_combination,
        best_weight,
        best_value,
        candidates_examined,
        feasible_solutions
    )


def main():
    packages = [
        ("P1", 2, 30),
        ("P2", 3, 40),
        ("P3", 4, 50),
        ("P4", 5, 60),
        ("P5", 1, 15),
        ("P6", 2, 25)
    ]

    capacity = 8

    print("DAA Assignment 2 - Q6: Exhaustive Search")
    print("-" * 50)

    start_time = time.perf_counter()

    result = exhaustive_search(packages, capacity)

    elapsed = time.perf_counter() - start_time

    combination, weight, value, candidates, feasible = result

    print("Payload capacity:", capacity)
    print("Selected packages:", combination)
    print("Total weight:", weight)
    print("Total humanitarian value:", value)
    print("Candidate combinations:", candidates)
    print("Feasible combinations:", feasible)
    print("Execution time:", round(elapsed, 6), "seconds")

    print("\nGrowth Investigation")
    print("-" * 50)

    for n in [5, 10, 15, 20]:
        print(
            "Packages:", n,
            "| Candidate combinations:", 2 ** n
        )


if __name__ == "__main__":
    main()
