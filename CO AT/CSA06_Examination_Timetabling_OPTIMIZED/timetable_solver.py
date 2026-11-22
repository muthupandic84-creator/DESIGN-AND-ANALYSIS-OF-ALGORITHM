"""
CSA06 - Examination Timetabling
Backtracking feasibility solver and optimal same-day penalty timetable.

Run:
    python timetable_solver.py
"""

from itertools import combinations

COURSES = {
    "C1": ("Design and Analysis of Algorithms", 120),
    "C2": ("Operating Systems", 90),
    "C3": ("Database Management Systems", 110),
    "C4": ("Computer Networks", 60),
    "C5": ("Java Programming", 150),
    "C6": ("Discrete Mathematics", 80),
    "C7": ("Artificial Intelligence", 40),
    "C8": ("Cloud Computing", 70),
}

CLASHES = {
    frozenset(pair) for pair in [
        ("C1", "C2"), ("C1", "C3"), ("C2", "C3"),
        ("C1", "C5"), ("C3", "C5"), ("C2", "C4"),
        ("C4", "C6"), ("C5", "C6"), ("C6", "C7"),
        ("C7", "C8"), ("C3", "C8"), ("C5", "C8"),
        ("C1", "C6"),
    ]
}

SLOTS = ["S1", "S2", "S3", "S4"]
SLOT_DAY = {"S1": 1, "S2": 1, "S3": 2, "S4": 2}
HALL_CAPACITY = {"A": 160, "B": 120}


def has_clash(a, b):
    return frozenset((a, b)) in CLASHES


def backtracking_timetable():
    """Find one feasible assignment using backtracking."""
    degree = {
        c: sum(c in edge for edge in CLASHES)
        for c in COURSES
    }
    order = sorted(COURSES, key=lambda c: (-degree[c], c))
    slots = {s: {} for s in SLOTS}  # hall -> course
    assignment = {}

    def search(i):
        if i == len(order):
            return True

        course = order[i]
        students = COURSES[course][1]

        for slot in SLOTS:
            if any(has_clash(course, other) for other in slots[slot].values()):
                continue

            for hall in ("B", "A"):
                if hall in slots[slot]:
                    continue
                if students > HALL_CAPACITY[hall]:
                    continue

                slots[slot][hall] = course
                assignment[course] = (slot, hall)

                if search(i + 1):
                    return True

                del slots[slot][hall]
                del assignment[course]

        return False

    return (slots, assignment) if search(0) else (None, None)


def day_penalty(group):
    return sum(1 for a, b in combinations(group, 2) if has_clash(a, b))


def valid_pairings(group):
    """Return all ways to split four courses into two non-clashing pairs."""
    a, b, c, d = group
    candidates = [
        ((a, b), (c, d)),
        ((a, c), (b, d)),
        ((a, d), (b, c)),
    ]
    return [
        pairing for pairing in candidates
        if not has_clash(*pairing[0]) and not has_clash(*pairing[1])
    ]


def find_optimal_timetable():
    """Exhaustively examine day partitions and legal session pairings."""
    names = list(COURSES)
    best_penalty = None
    best_slots = None
    best_partition = None

    for day1 in combinations(names, 4):
        day1_set = set(day1)
        day2 = tuple(c for c in names if c not in day1_set)

        pairings1 = valid_pairings(day1)
        pairings2 = valid_pairings(day2)
        if not pairings1 or not pairings2:
            continue

        penalty = day_penalty(day1) + day_penalty(day2)
        if best_penalty is not None and penalty >= best_penalty:
            continue

        # Choose a valid pairing for each day. Each pair is one session.
        p1 = pairings1[0]
        p2 = pairings2[0]
        best_penalty = penalty
        best_partition = (day1, day2)
        best_slots = {
            "S1": p1[0],
            "S2": p1[1],
            "S3": p2[0],
            "S4": p2[1],
        }

    if best_slots is None:
        return None, None, None

    # Assign halls within each session. Hall A is mandatory for 150 students.
    optimal = {}
    for slot, pair in best_slots.items():
        hall_assignment = {}
        remaining = list(pair)
        # Put the largest course in Hall A; the other course goes to Hall B
        # when it fits, otherwise use the remaining feasible allocation.
        remaining.sort(key=lambda c: COURSES[c][1], reverse=True)
        for course in remaining:
            students = COURSES[course][1]
            available = [
                h for h in ("A", "B")
                if h not in hall_assignment and students <= HALL_CAPACITY[h]
            ]
            if not available:
                raise RuntimeError(f"No valid hall for {course} in {slot}")
            # Prefer Hall A for the larger course, Hall B for the smaller one.
            hall = available[0] if len(available) == 1 else (
                "A" if students > HALL_CAPACITY["B"] else "B"
            )
            hall_assignment[hall] = course
        optimal[slot] = hall_assignment

    return best_penalty, best_partition, optimal


def print_timetable(title, slots):
    print("\n" + title)
    for slot in SLOTS:
        print(f"\n{slot} (Day {SLOT_DAY[slot]})")
        for hall in ("A", "B"):
            course = slots[slot].get(hall)
            if course is None:
                print(f"  Hall {hall}: Empty")
            else:
                name, students = COURSES[course]
                print(f"  Hall {hall}: {course} - {name} ({students} students)")


def verify(slots):
    assigned = [course for slot in SLOTS for course in slots[slot].values()]
    assert len(assigned) == len(COURSES)
    assert set(assigned) == set(COURSES)

    for a, b in CLASHES:
        for slot in SLOTS:
            assert not (a in slots[slot].values() and b in slots[slot].values())

    for slot in SLOTS:
        assert len(slots[slot]) <= 2
        for hall, course in slots[slot].items():
            assert COURSES[course][1] <= HALL_CAPACITY[hall]


def main():
    feasible_slots, _, = backtracking_timetable()
    if feasible_slots is None:
        print("No feasible timetable exists.")
        return

    print_timetable("BACKTRACKING FEASIBILITY RESULT", feasible_slots)
    verify(feasible_slots)
    print("\nFeasible timetable: all hard constraints verified.")

    penalty, partition, optimal_slots = find_optimal_timetable()
    if optimal_slots is None:
        print("No optimised timetable found.")
        return

    verify(optimal_slots)
    print_timetable("OPTIMAL TIMETABLE (BRANCH AND BOUND / EXACT SMALL-INSTANCE SEARCH)",
                    optimal_slots)
    print("\nOPTIMISATION RESULT")
    print("Minimum same-day clash penalty:", penalty)
    print("Day 1 courses:", ", ".join(partition[0]))
    print("Day 2 courses:", ", ".join(partition[1]))
    print("Optimal timetable hard-constraint verification: PASSED")
    print("\nThree sessions are impossible: 3 sessions x 2 halls = 6 places,")
    print("but 8 examinations must be scheduled.")


if __name__ == "__main__":
    main()
