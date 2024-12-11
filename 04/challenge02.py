from enum import Enum

def main(fname: str):
    chars = []
    with open(fname, "r") as file:
        chars = parse(file.read())
    haystack = HayStack(chars)
    print(haystack.needle_count("XMAS"))

def parse(data: str) -> list[list[str]]:
    i = 0
    chars = []
    for line in data.split("\n"):
        chars.append([])
        for char in line:
            chars[i].append(char)
        i += 1
    return chars

class HayStack:
    def __init__(self, hay: list[list[str]]):
        self.hay = hay
        self.count = 0

    def nearest_points(self, p: tuple[int]) -> list[tuple[int] | None]:
        points = []
        for dir in Direction:
            if dir != Direction.ALL:
                points.append(self.nearest_point(p, dir))
        return points

    def nearest_point(self, p: tuple[int], dir) -> list[tuple[int] | None]:
        max_x = len(self.hay[0]) - 1
        max_y = len(self.hay) - 1
        if p is None:
            return None
        match dir:
            case Direction.ALL:
                return self.nearest_points(p)
            case Direction.N:
                if (y := p[1] - 1) >= 0:
                    return (p[0], y)
                else: return None
            case Direction.E:
                if (x := p[0] + 1) <= max_x:
                    return (x, p[1])
                else: return None
            case Direction.S:
                if (y := p[1] + 1) <= max_y:
                    return (p[0], y)
                else: return None
            case Direction.W:
                if (x := p[0] - 1) >= 0:
                    return (x, p[1])
                else: return None
            case Direction.NE:
                y = self.nearest_point(p, Direction.N)
                x = self.nearest_point(p, Direction.E)
                if not (y is None or x is None):
                    return (x[0], y[1])
                else: return None
            case Direction.SE:
                y = self.nearest_point(p, Direction.S)
                x = self.nearest_point(p, Direction.E)
                if not (y is None or x is None):
                    return (x[0], y[1])
                else: return None
            case Direction.SW:
                y = self.nearest_point(p, Direction.S)
                x = self.nearest_point(p, Direction.W)
                if not (y is None or x is None):
                    return (x[0], y[1])
                else: return None
            case Direction.NW:
                y = self.nearest_point(p, Direction.N)
                x = self.nearest_point(p, Direction.W)
                if not (y is None or x is None):
                    return (x[0], y[1])
                else: return None
            
    def get_direction(self, a: tuple[int], b: tuple[int]):
        if (a is None) or (b is None):
            return Direction.ALL
        if a == b:
            return Direction.ALL
        x0, y0 = a
        x1, y1 = b
        if (x0 == x1) and (y1 < y0):
            return Direction.N
        elif (x0 == x1) and (y1 > y0):
            return Direction.S
        elif (x1 > x0) and (y0 == y1):
            return Direction.E
        elif (x1 < x0) and (y0 == y1):
            return Direction.W
        elif (x1 > x0) and (y1 < y0):
            return Direction.NE
        elif (x1 > x0) and (y1 > y0):
            return Direction.SE
        elif (x1 < x0) and (y1 > y0):
            return Direction.SW
        elif (x1 < x0) and (y1 < y0):
            return Direction.NW

    def needle_count(self, needle: str) -> int:
        [x, y, pos] = [0, 0, 0]
        for line in self.hay:
            x = 0
            for char in line:
                self.count += self.find((x, y), needle, Direction.ALL)
                x += 1
            y += 1
        return self.count
    
    def find(self, p, needle, dir, i = 0):
        x = 0
        if self.hay[p[1]][p[0]] == needle[i]:
            for point in self.nearest_points(p):
                if self.find_next(point, needle, self.get_direction(p, point), i+1):
                    x += 1
        return x

    
    def find_next(self, p: tuple[int], needle: str, dir, i: int = 0) -> bool:
        if p is None:
            return False
        if (x := self.hay[p[1]][p[0]]) == needle[i]:
            if i == len(needle) - 1:
                return True
            else:
                point = self.nearest_point(p, dir)
                return self.find_next(point, needle, dir, i+1)
        else:
            return False

class Direction(Enum):
    ALL = 0
    N   = 1
    NE  = 2
    E   = 3
    SE  = 4
    S   = 5
    SW  = 6
    W   = 7
    NW  = 8



if __name__ == "__main__":
    main("input.txt")