import csv
from pathlib import Path
import matplotlib.pyplot as plt


input_file = "../results/results.csv"

rows = []

with open(input_file, newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        rows.append(row)


algorithms = [
    "Linear Search",
    "Binary Search",
    "Hash Table"
]

sizes = [
    1000,
    10000,
    100000,
    1000000
]


Path("../results/graphs").mkdir(
    parents=True,
    exist_ok=True
)


def average(algorithm, size, column):

    values = []

    for row in rows:

        if (
            row["Algorithm"] == algorithm
            and int(row["Dataset_Size"]) == size
        ):
            values.append(
                float(row[column])
            )

    return sum(values) / len(values)


# Runtime graph

plt.figure(figsize=(8, 5))

for algorithm in algorithms:

    values = [
        average(
            algorithm,
            size,
            "Time_Seconds"
        )
        for size in sizes
    ]

    plt.plot(
        sizes,
        values,
        marker="o",
        label=algorithm
    )

plt.xlabel("Number of Records")
plt.ylabel("Execution Time (seconds)")
plt.title("Search Algorithm Runtime Comparison")
plt.xscale("log")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../results/graphs/runtime_graph.png",
    dpi=200
)

plt.close()


# Comparison graph

plt.figure(figsize=(8, 5))

for algorithm in algorithms:

    values = [
        average(
            algorithm,
            size,
            "Comparisons_or_Operations"
        )
        for size in sizes
    ]

    plt.plot(
        sizes,
        values,
        marker="o",
        label=algorithm
    )

plt.xlabel("Number of Records")
plt.ylabel("Comparisons / Key Operations")
plt.title("Search Operation Comparison")
plt.xscale("log")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../results/graphs/comparisons_graph.png",
    dpi=200
)

plt.close()

print("Graphs generated successfully.")
