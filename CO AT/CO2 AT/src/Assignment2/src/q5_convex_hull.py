# DAA Assignment 2
# Q5: Brute-Force Convex Hull
# Problem: Wildlife Reserve Boundary Monitoring

import matplotlib.pyplot as plt


def cross_product(a, b, c):
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )


def brute_force_convex_hull(points):
    hull_edges = set()
    comparisons = 0
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            positive = False
            negative = False

            for k in range(n):
                if k == i or k == j:
                    continue

                comparisons += 1
                value = cross_product(
                    points[i], points[j], points[k]
                )

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

                if positive and negative:
                    break

            if not (positive and negative):
                hull_edges.add((i, j))

    return hull_edges, comparisons


def main():
    test_cases = {
        "Boundary and interior points": [
            (0, 0), (4, 0), (4, 4), (0, 4),
            (2, 2), (1, 2), (3, 1)
        ],
        "Irregular point configuration": [
            (0, 2), (2, 5), (5, 4), (6, 1),
            (3, 0), (2, 2), (4, 2), (1, 1)
        ]
    }

    for name, points in test_cases.items():
        edges, comparisons = brute_force_convex_hull(points)

        print("\nTest:", name)
        print("Points:", points)
        print("Candidate hull edges:", len(edges))
        print("Orientation tests:", comparisons)

        plt.figure()
        x_values = [p[0] for p in points]
        y_values = [p[1] for p in points]

        plt.scatter(
            x_values, y_values,
            label="Monitoring stations"
        )

        for i, j in edges:
            x = [points[i][0], points[j][0]]
            y = [points[i][1], points[j][1]]
            plt.plot(x, y)

        plt.title(name)
        plt.xlabel("X coordinate")
        plt.ylabel("Y coordinate")
        plt.grid(True)
        plt.legend()
        plt.axis("equal")

        filename = name.lower().replace(" ", "_") + ".png"
        plt.savefig(filename, dpi=150, bbox_inches="tight")
        print("Graph saved as:", filename)

        plt.show()


if __name__ == "__main__":
    main()
