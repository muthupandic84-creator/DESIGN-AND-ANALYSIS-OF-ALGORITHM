# DAA Assignment 2
# Q3: Brute-Force String Matching
# Problem: Cybersecurity Log Screening

def brute_force_matching(text, pattern):
    comparisons = 0
    positions = []

    if pattern == "":
        return positions, comparisons

    for i in range(len(text) - len(pattern) + 1):
        j = 0

        while j < len(pattern):
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == len(pattern):
            positions.append(i)

    return positions, comparisons


def main():
    print("DAA Assignment 2 - Q3: Brute-Force String Matching")
    print("-" * 55)

    test_cases = [
        ("securitylog", "log"),
        ("aaaaaaaaaa", "aaaab"),
        ("system_error_system_error", "error")
    ]

    for number, (text, pattern) in enumerate(test_cases, start=1):
        positions, comparisons = brute_force_matching(text, pattern)

        print("\nTest Case", number)
        print("Text:", text)
        print("Pattern:", pattern)
        print("Matching positions:", positions)
        print("Character comparisons:", comparisons)


if __name__ == "__main__":
    main()
