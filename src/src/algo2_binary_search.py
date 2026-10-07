REG_NO = "192565037"
NAME = "Muthupandi C"


def binary_search(records, key, low, high, comparisons=0):

    if low > high:
        return -1, comparisons

    mid = (low + high) // 2

    comparisons += 1

    if records[mid] == key:
        return mid, comparisons

    elif key < records[mid]:
        return binary_search(
            records,
            key,
            low,
            mid - 1,
            comparisons
        )

    else:
        return binary_search(
            records,
            key,
            mid + 1,
            high,
            comparisons
        )


if __name__ == "__main__":

    records = [101, 205, 309, 412, 518]

    key = int(input("Enter registration number to search: "))

    position, comparisons = binary_search(
        records,
        key,
        0,
        len(records) - 1
    )

    print("========================================")
    print("DAA ASSIGNMENT 1")
    print("Name:", NAME)
    print("Reg No:", REG_NO)
    print("========================================")

    if position != -1:
        print("Search Result: FOUND")
        print("Position:", position + 1)
    else:
        print("Search Result: NOT FOUND")

    print("Comparisons:", comparisons)
