"""Correctness and boundary tests for sentinelops.py."""
from math import isclose, isinf
from sentinelops import (
    sort_alerts, build_blocklist_index, is_blocked,
    find_signature, closest_logins
)


def run_tests():
    # Stable descending insertion sort; caller's list remains unchanged.
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    assert sort_alerts(alerts) == [
        ("A2", 9), ("A4", 9), ("A3", 5), ("A1", 3), ("A5", 1)
    ]
    assert alerts[0] == ("A1", 3)

    # Blocklist: present, absent, empty and pre-built set.
    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    assert [is_blocked(blocklist, ip) for ip in
            ("10.0.0.9", "10.0.0.5", "8.8.8.8")] == [True, True, False]
    indexed = build_blocklist_index(blocklist)
    assert is_blocked(indexed, "10.0.0.9") is True
    assert is_blocked([], "10.0.0.9") is False

    # Brute-force signature matching: beginning, end, mismatch, overlap.
    assert find_signature("FAILFAIXFAIL", "FAIL") == [0, 8]
    assert find_signature("ABCEND", "END") == [3]
    assert find_signature("ABC", "ABCDE") == []
    assert find_signature("AAAA", "AA") == [0, 1, 2]
    assert find_signature("ABC", "") == [0, 1, 2, 3]
    assert find_signature("", "A") == []

    # Closest pair: expected sample, fewer than two points, duplicates.
    events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    pair, distance = closest_logins(events)
    assert set(pair) == {0, 5}
    assert isclose(distance, 2 ** 0.5, rel_tol=1e-9)

    assert closest_logins([]) == (None, float("inf"))
    pair, distance = closest_logins([(0, 0)])
    assert pair is None and isinf(distance)

    pair, distance = closest_logins([(0, 0), (3, 4)])
    assert set(pair) == {0, 1}
    assert isclose(distance, 5.0)

    pair, distance = closest_logins([(1, 1), (1, 1), (8, 8)])
    assert distance == 0.0

    print("All SentinelOps tests passed.")


if __name__ == "__main__":
    run_tests()
