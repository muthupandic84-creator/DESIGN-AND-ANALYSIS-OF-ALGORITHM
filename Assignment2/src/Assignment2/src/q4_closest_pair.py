# DAA Assignment 2
# Q4: Brute-Force Closest Pair
# Problem: Drone Collision-Risk Monitoring

import math
import random
import time


def closest_pair(points):
    minimum_distance = float("inf")
    closest_points = None
    pairs_examined = 0
    distance_calculations = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs_examined += 1

            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = math.sqrt(
                (x2 - x1) ** 2 + (y2 - y1) ** 2
            )

            distance_calculations += 1

            if distance < minimum_distance:
                minimum_distance = distance
                closest_points = (points[i], points[j])

    return (
        closest_points,
        minimum_distance,
        pairs_examined,
        distance_calculations
    )


def main():
    print("DAA Assignment 2 - Q4: Brute-Force Closest Pair")
    print("-" * 55)

    test_sizes = [10, 100, 500]

    for size in test_sizes:
        random.seed(5037 + size)

        points = [
            (random.randint(0, 10000), random.randint(0, 10000))
            for _ in range(size)
        ]

        start_time = time.perf_counter()

        pair, distance, pairs, calculations = closest_pair(points)

        elapsed = time.perf_counter() - start_time

        print("\nNumber of drones:", size)
        print("Closest pair:", pair)
        print("Minimum distance:", round(distance, 4))
        print("Pairs examined:", pairs)
        print("Distance calculations:", calculations)
        print("Execution time:", round(elapsed, 6), "seconds")

        expected_pairs = size * (size - 1) // 2
        print("Theoretical pair count:", expected_pairs)


if __name__ == "__main__":
    main()
