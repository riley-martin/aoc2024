import re

def main(fname: str):
    results = []
    with open(fname, "r") as program:
        for line in program:
            results.append(execute(line))
    print(sum(results))

def execute(line: str) -> int:
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total

if __name__ == "__main__":
    main("./input.txt")