# DAA Assignment 1
## Design and Analysis of Algorithms

### Student Details

- **Name:** Muthupandi C
- **Register Number:** 192565037
- **Course:** Design and Analysis of Algorithms
- **Assignment:** Assignment 1
- **Personal Seed:** 5037

### Problem Statement

Design, analyse and validate an efficient search strategy for a large-scale student record system.

The system searches student registration numbers in datasets ranging from:

- 1,000 records
- 10,000 records
- 100,000 records
- 1,000,000 records

### Algorithms Used

Three different search strategies are implemented:

1. **Linear Search**
   - Iterative approach
   - Time Complexity: O(n)

2. **Binary Search**
   - Recursive approach
   - Requires sorted data
   - Time Complexity: O(log n)

3. **Hash Table Search**
   - Uses a hash table for direct lookup
   - Average search complexity: O(1)
   - Requires preprocessing

### Test Cases

**Found Registration Number:**

192565037

**Not Found Registration Number:**

192565038

### Dataset Sizes

The algorithms are tested using:

- 1,000 records
- 10,000 records
- 100,000 records
- 1,000,000 records

### Dataset Generation

The datasets are generated using a deterministic seed based on the last four digits of the register number.

- **Register Number:** 192565037
- **Personal Seed:** 5037

### How to Run

Open the `src` folder in the terminal.

Generate the datasets:

```text
python dataset_generator.py
python benchmark.py
python plot_results.py
### Experimental Evaluation

The algorithms are compared using:

- Execution time
- Number of comparisons
- Dataset size
- Preprocessing time
- Found and not-found searches

### Task 12

The changed requirement is 50,000 searches per hour on 1,000,000 student records, with new records added only once per day.

The experimental and theoretical analysis is used to determine whether the selected search strategy should be retained, modified or redesigned.

### Project Structure

```text
DAA-A1-192565037-MuthupandiC/
├── README.md
├── report/
├── src/
│   ├── algo1_linear_search.py
│   ├── algo2_binary_search.py
│   ├── algo3_hash_table.py
│   ├── dataset_generator.py
│   ├── benchmark.py
│   └── plot_results.py
├── data/
├── results/
└── screenshots/
