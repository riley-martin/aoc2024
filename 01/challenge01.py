def main(fname: str):
    list1 = []
    list2 = []
    with open(fname, "r") as places:
        for line in places:
            parse(line, list1, list2)
    [list1, list2] = [sorted(list1), sorted(list2)]
    distance = sum_of_difference(list1, list2)
    print(distance)

# Lists must be the same length
def sum_of_difference(list1: list[int], list2: list[int]) -> int:
    total_distance = 0
    for i, j in zip(list1, list2):
        distance = abs(i - j)
        total_distance += distance
    return total_distance

def parse(line: str, list1: list[int], list2: list[int]):
    # Split on three spaces
    [value1, value2] = line.split("   ")
    list1.append(int(value1))
    list2.append(int(value2))

if __name__ == "__main__":
    main("./input01.txt")