# DAA Assignment 2
# Q2: Sequential Search
# Aircraft Maintenance Tool Tracking

def sequential_search(tools, target):
    comparisons = 0

    for tool in tools:
        comparisons += 1

        if tool == target:
            return True, comparisons

    return False, comparisons


def main():
    tools = ["T-101", "T-102", "T-103", "T-184", "T-205"]

    print("DAA Assignment 2 - Q2: Sequential Search")

    target = input("Enter Tool ID to search: ")

    found, comparisons = sequential_search(tools, target)

    if found:
        print("Tool found.")
    else:
        print("Tool not found.")

    print("Number of comparisons:", comparisons)

    print("\nExperimental Tests")

    test_cases = [
        ("First position", "T-101"),
        ("Middle position", "T-103"),
        ("Last position", "T-205"),
        ("Unsuccessful search", "T-999")
    ]

    for description, target in test_cases:
        found, comparisons = sequential_search(tools, target)

        print(description)
        print("Target:", target)
        print("Found:", found)
        print("Comparisons:", comparisons)
        print()


if __name__ == "__main__":
    main()
