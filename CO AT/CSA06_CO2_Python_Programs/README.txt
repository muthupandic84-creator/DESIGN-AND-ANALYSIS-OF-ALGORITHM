SENTINELOPS – CSA06 CO2 PROGRAM FILES

Files
-----
sentinelops.py
    Corrected algorithms:
    1. Stable insertion sort for severity (highest first)
    2. Blocklist membership and set-index builder
    3. Brute-force signature search (includes final position and overlaps)
    4. Divide-and-conquer closest pair of 2-D login locations

test_sentinelops.py
    Test harness for normal and boundary cases.

benchmark.py
    Counts insertion-sort comparisons for nearly sorted and random alerts.
    Also compares the brute-force closest-pair pair-count formula with the
    elapsed time of the divide-and-conquer implementation.

Requirements
------------
Python 3.9 or later. No third-party packages are required.

Run the sample program
----------------------
python sentinelops.py

Run all correctness tests
-------------------------
python test_sentinelops.py

Expected test result
--------------------
All SentinelOps tests passed.

Run benchmarks
--------------
python benchmark.py

Important notes
---------------
- The module's sorting function retains stable insertion sort to demonstrate
  the assessed algorithm. For a 50,000-alert production feed, Python's stable
  built-in sorted() is generally preferable because it has O(n log n)
  worst-case performance and is highly optimised.
- For repeated blocklist queries, build the set once:
      blocked_index = build_blocklist_index(blocklist)
  Then call is_blocked(blocked_index, source_ip).
- The closest-pair function returns (None, infinity) when fewer than two
  events are supplied.
- Benchmark timings depend on the computer and Python version. Record your
  own lab-machine results in the assignment report.
