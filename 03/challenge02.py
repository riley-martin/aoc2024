import re

def main(fname: str):
    results = []
    with open(fname, "r") as program:
        results = execute(program.read())
    print(results)

def execute(line: str) -> int:
    pat = re.compile(r"(?P<mul>mul\((\d+),(\d+)\))|(?P<do>do\(\))|(?P<dont>don't\(\))")
    total = 0
    enabled = True
    for m in re.finditer(pat, line):
        match m.groupdict():
            case {"do": "do()"}:
                enabled = True
            case {"dont": "don't()"}:
                enabled = False
            case {"mul": x}:
                if enabled:
                    subm = re.search(r"mul\((\d+),(\d+)\)", x)
                    total += int(subm[1]) * int(subm[2])
            case _:
                continue
    return total

if __name__ == "__main__":
    main("./input.txt")