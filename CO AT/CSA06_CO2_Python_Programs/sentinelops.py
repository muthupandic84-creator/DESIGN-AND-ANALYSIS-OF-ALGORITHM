"""
SentinelOps SOC alert-triage algorithms.
Python 3.9+
"""
import math
from math import inf


def sort_alerts(alerts):
    """
    Return alerts in descending severity order using stable insertion sort.
    Equal-severity alerts retain their original arrival order.
    The input list is not modified.
    """
    result = list(alerts)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j][1] < key[1]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def build_blocklist_index(blocklist):
    """Build a set for efficient repeated blocklist membership checks."""
    return set(blocklist)


def is_blocked(blocklist, ip):
    """
    Return True if ip is present in the supplied list, set, or frozenset.
    A set is recommended when many lookups will be performed.
    """
    return ip in blocklist


def find_signature(log, pattern):
    """
    Return all starting indexes where pattern occurs in log.
    Overlapping matches are included. An empty pattern matches every
    boundary position from 0 through len(log).
    """
    if pattern == "":
        return list(range(len(log) + 1))

    n, m = len(log), len(pattern)
    hits = []

    # +1 includes the final legal starting position n-m.
    for i in range(n - m + 1):
        j = 0
        while j < m and log[i + j] == pattern[j]:
            j += 1
        # A hit is recorded only if every pattern character matched.
        if j == m:
            hits.append(i)

    return hits


def closest_logins(events):
    """
    Return ((i, j), distance) for the closest pair of 2-D login locations.

    Uses divide-and-conquer in O(n log n) time. Coordinates are (x, y)
    values in kilometres. For fewer than two events, returns (None, inf).
    The indexes in the returned pair refer to the original input sequence.
    """
    n = len(events)
    if n < 2:
        return None, inf

    points = [(point[0], point[1], index)
              for index, point in enumerate(events)]
    by_x = sorted(points, key=lambda p: (p[0], p[1], p[2]))
    by_y = sorted(points, key=lambda p: (p[1], p[0], p[2]))

    def squared_distance(p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

    def brute_force(small_points):
        best_d2 = inf
        best_pair = None
        for i in range(len(small_points)):
            for j in range(i + 1, len(small_points)):
                p, q = small_points[i], small_points[j]
                d2 = squared_distance(p, q)
                if d2 < best_d2:
                    best_d2 = d2
                    best_pair = (p[2], q[2])
        return best_d2, best_pair

    def solve(px, py):
        size = len(px)
        if size <= 3:
            return brute_force(px)

        middle = size // 2
        left_x = px[:middle]
        right_x = px[middle:]
        left_ids = {p[2] for p in left_x}
        split_x = right_x[0][0]

        left_y = []
        right_y = []
        for point in py:
            if point[2] in left_ids:
                left_y.append(point)
            else:
                right_y.append(point)

        left_d2, left_pair = solve(left_x, left_y)
        right_d2, right_pair = solve(right_x, right_y)

        if left_d2 <= right_d2:
            best_d2, best_pair = left_d2, left_pair
        else:
            best_d2, best_pair = right_d2, right_pair

        # Points farther than the current best distance from the split
        # cannot improve the answer.
        strip = [p for p in py if (p[0] - split_x) ** 2 < best_d2]

        # The strip is already sorted by y. The geometric packing argument
        # bounds the number of following points worth checking.
        for i in range(len(strip)):
            j = i + 1
            while (j < len(strip)
                   and (strip[j][1] - strip[i][1]) ** 2 < best_d2):
                d2 = squared_distance(strip[i], strip[j])
                if d2 < best_d2:
                    best_d2 = d2
                    best_pair = (strip[i][2], strip[j][2])
                j += 1

        return best_d2, best_pair

    best_d2, pair = solve(by_x, by_y)
    return pair, math.sqrt(best_d2)


if __name__ == "__main__":
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    log = "FAILFAIXFAIL"
    pattern = "FAIL"
    events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

    print("Sorted alerts:", sort_alerts(alerts))
    print("Blocklist checks:", [
        is_blocked(blocklist, ip)
        for ip in ("10.0.0.9", "10.0.0.5", "8.8.8.8")
    ])
    print("Signature positions:", find_signature(log, pattern))
    print("Closest logins:", closest_logins(events))
