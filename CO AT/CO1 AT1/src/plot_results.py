import csv
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

input_file = Path("../results/results.csv")
graph_dir = Path("../results/graphs")
graph_dir.mkdir(parents=True, exist_ok=True)

runtime_data = defaultdict(list)
comparison_data = defaultdict(list)

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        size = int(row["Dataset_Size"])
        algorithm = row["Algorithm"]

        runtime_data[algorithm].append(
            (size, float(row["Runtime_Seconds"]))
        )

        comparison_data[algorithm].append(
            (size, int(row["Comparisons"]))
        )

# Runtime graph
plt.figure(figsize=(9, 6))

for algorithm, values in runtime_data.items():
    values.sort()
    x = [v[0] for v in values]
    y = [v[1] for v in values]
    plt.plot(x, y, marker="o", label=algorithm)

plt.xlabel("Dataset Size")
plt.ylabel("Runtime (seconds)")
plt.title("Search Algorithm Runtime Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(graph_dir / "runtime_graph.png", dpi=200)
plt.close()

# Comparisons graph
plt.figure(figsize=(9, 6))

for algorithm, values in comparison_data.items():
    values.sort()
    x = [v[0] for v in values]
    y = [v[1] for v in values]
    plt.plot(x, y, marker="o", label=algorithm)

plt.xlabel("Dataset Size")
plt.ylabel("Number of Comparisons")
plt.title("Search Algorithm Comparison Count")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(graph_dir / "comparisons_graph.png", dpi=200)
plt.close()

print("Graphs generated successfully.")
print("Saved in:", graph_dir)
