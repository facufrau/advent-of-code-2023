# --- Day 3: Gear Ratios ---

# Part one and two
import re
with open('input03.txt') as f:
    engine = [list(x.strip()) for x in f.readlines()]

class Part(object):
    def __init__(self, coords, val):
        self.startx = coords[0]
        self.endx = coords[1]
        self.coordy = coords[2]
        self.value = val
    
    def __repr__(self):
        return f"Value: {self.value}"

    def is_adjacent_to(self, symbol_obj):
        delta = [(-1,-1),(0,-1),(1,-1),
                 (-1, 0),       (1, 0),
                 (-1, 1),(0, 1),(1, 1),]
        for x in range(self.startx, self.endx + 1):
            for d in delta:
                inc_coords = (x + d[0], self.coordy + d[1])
                checkx = inc_coords[0] == symbol_obj.coords[0]
                checky = inc_coords[1] == symbol_obj.coords[1]
                if checkx and checky:
                    # For part two
                    symbol_obj.add_gear(self.value)
                    return True
        return False
                   
class Symbol(object):
    def __init__(self, coords, char):
        self.coords = coords
        self.gears = []
        self.char = char
    
    # For part two
    def add_gear(self, value):
        self.gears.append(value)

    def __repr__(self):
        return f"X: {self.coords[0]} - Y {self.coords[1]}"

parts = []
symbols = []
for y, line in enumerate(engine):
    start = None
    end = None
    # Parsing the parts numbers
    line_str = ''.join(line)
    numbs = re.finditer("\d+",line_str)
    for n in numbs:
        coords = (n.start(), n.end()-1, y)
        parts.append(Part(coords, int(n.group(0))))
    
    # Parsing the symbols
    for x, char in enumerate(line):
        if char != '.' and (not char.isdigit()):
            symbols.append(Symbol((x, y), char))

# Part one solution
total = 0
for part in parts:
    for symbol in symbols:
        if part.is_adjacent_to(symbol):
            total += part.value
print(f"Part one answer: Total sum of part values --> {total}")

# Part two solution
gear_ratio_total = 0
for symbol in symbols:
    if symbol.char == '*' and len(symbol.gears) == 2:
        gear_ratio_total += (symbol.gears[0] * symbol.gears[1])
print(f"Part two answer: Total sum of gear ratios--> {gear_ratio_total}")




