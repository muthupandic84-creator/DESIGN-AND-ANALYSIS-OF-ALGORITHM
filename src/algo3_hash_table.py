REG_NO = "192565037"
NAME = "Muthupandi C"

def build_hash_table(records):
    hash_table = {}

    for index, value in enumerate(records):
        hash_table[value] = index

    return hash_table


def hash_search(hash_table, key):
    if key in hash_table:
        return hash_table[key], 1

    return -1, 1


if __name__ == "__main__":
    records = [101, 205, 309, 412, 518]

    hash_table = build_hash_table(records)

    key = int(input("Enter registration number to search: "))

    position, comparisons = hash_search(hash_table, key)

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

    print("Hash Lookup Operations:", comparisons)
