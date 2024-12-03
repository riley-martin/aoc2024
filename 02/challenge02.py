def main(fname: str):
    reports = []
    with open(fname, "r") as data:
        for line in data:
            parse(line, reports)
    safe_reports = check_safety(reports)
    print(safe_reports)
    n_safe = safe_reports.count(True)
    print(n_safe)

def check_safety(reports: list[list[int]]) -> list[bool]:
    safety = []
    for report in reports:
        safe = True
        if not is_safe(report):
            safe = False
            report_safety = []
            for i in range(len(report)):
                part_report = report[:i] + report[i + 1:]
                report_safety.append(is_safe(part_report))
            if any(report_safety):
                safe = True
        safety.append(safe)
    return safety

def parse(line: str, reports: list[list[int]]):
    reports.append([int(i) for i in line.split(" ")])

def is_safe(l: list) -> bool:
    return ((all(a <= b for a, b in zip(l, l[1:])) or all(a >= b for a, b in zip(l, l[1:])))
        and all(1 <= abs(a - b) <= 3 for a, b in zip(l, l[1:])))

if __name__ == "__main__":
    main("./input.txt")
