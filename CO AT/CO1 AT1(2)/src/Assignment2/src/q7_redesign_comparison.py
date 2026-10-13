# DAA Assignment 2
# Q7: Diagnose, Redesign and Validate
# Original: Brute-Force Closest Pair
# Redesigned: Divide-and-Conquer Closest Pair

import math
import random
import time


def distance(point1, point2):
    return math.hypot(
        point1[0] - point2[0],
        point1[1] - point2[1]
    )


def brute_force(points):
    minimum_distance = float("inf")
    closest_points = None
    comparisons = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            comparisons += 1
            current_distance = distance(points[i], points[j])

            if current_distance < minimum_distance:
                minimum_distance = current_distance
                closest_points = (points[i], points[j])

    return closest_points, minimum_distance, comparisons


def divide_and_conquer(points):
    sorted_points = sorted(points, key=lambda point: point[0])
    distance_calculations = 0

    def calculate_distance(point1, point2):
        nonlocal distance_calculations
        distance_calculations += 1
        return distance(point1, point2)

    def solve(points_x):
        n = len(points_x)

        if n <= 3:
            best_distance = float("inf")
            best_pair = None

            for i in range(n):
                for j in range(i + 1, n):
                    current_distance = calculate_distance(
                        points_x[i], points_x[j]
                    )

                    if current_distance < best_distance:
                        best_distance = current_distance
                        best_pair = (points_x[i], points_x[j])

            return best_pair, best_distance

        middle = n // 2
        middle_x = points_x[middle][0]

        left_pair, left_distance = solve(points_x[:middle])
        right_pair, right_distance = solve(points_x[middle:])

        if left_distance <= right_distance:
            best_pair = left_pair
            best_distance = left_distance
        else:
            best_pair = right_pair
            best_distance = right_distance

        strip = [
            point for point in points_x
            if abs(point[0] - middle_x) < best_distance
        ]

        strip.sort(key=lambda point: point[1])

        for i in range(len(strip)):
            j = i + 1

            while (
                j < len(strip)
                and strip[j][1] - strip[i][1] < best_distance
            ):
                current_distance = calculate_distance(
                    strip[i], strip[j]
                )

                if current_distance < best_distance:
                    best_distance = current_distance
                    best_pair = (strip[i], strip[j])

                j += 1

        return best_pair, best_distance

    pair, minimum_distance = solve(sorted_points)

    return pair, minimum_distance, distance_calculations


def main():
    print("DAA Assignment 2 - Q7")
    print("Original vs Redesigned Closest-Pair Algorithm")
    print("=" * 55)

    test_sizes = [100, 500, 1000]

    for size in test_sizes:
        random.seed(5037 + size)

        points = [
            (random.random() * 10000, random.random() * 10000)
            for _ in range(size)
        ]

        start_time = time.perf_counter()
        original_pair, original_distance, original_count = (
            brute_force(points)
        )
        original_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        redesigned_pair, redesigned_distance, redesigned_count = (
            divide_and_conquer(points)
        )
        redesigned_time = time.perf_counter() - start_time

        print("\nNumber of points:", size)
        print("-" * 40)

        print("Original pair comparisons:", original_count)
        print("Original execution time:",
              round(original_time, 6), "seconds")

        print("Redesigned distance calculations:", redesigned_count)
        print("Redesigned execution time:",
              round(redesigned_time, 6), "seconds")

        print("Original minimum distance:",
              round(original_distance, 6))

        print("Redesigned minimum distance:",
              round(redesigned_distance, 6))

        results_match = math.isclose(
            original_distance,
            redesigned_distance,
            rel_tol=1e-9,
            abs_tol=1e-9
        )

        print("Minimum distances agree:", results_match)


if __name__ == "__main__":
    main()
