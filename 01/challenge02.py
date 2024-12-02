def main(fname: str):
    list1 = []
    list2 = []
    with open(fname, "r") as places:
        for line in places:
            parse(line, list1, list2)
    score = similarity(list1, list2)
    print(score)

def similarity(list1: list[int], list2: list[int]) -> int:
    score = 0
    for i in list1:
        score += i * list2.count(i)
    return score

def parse(line: str, list1: list[int], list2: list[int]):
    # Split on three spaces
    [value1, value2] = line.split("   ")
    list1.append(int(value1))
    list2.append(int(value2))

if __name__ == "__main__":
    main("./input01.txt")