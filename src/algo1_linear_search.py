REG_NO = "192565037"
NAME = "Muthupandi C"


def linear_search(records, key):
    comparisons = 0

    for i in range(len(records)):
        comparisons += 1

        if records[i] == key:
            return i, comparisons

    return -1, comparisons


if __name__ == "__main__":

    records = [101, 205, 309, 412, 518]

    key = int(input("Enter registration number to search: "))

    position, comparisons = linear_search(records, key)

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
