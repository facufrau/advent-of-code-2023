# --- Day 2: Cube Conundrum ---

# Part one 
with open('input02.txt') as f:
    lines = f.readlines()

# For converting color names to list indexes in RGB.
convert = {"red": 0, "green": 1, "blue": 2}
total_sum = 0
total_power = 0
for line in lines:
    new_line = line.strip().split(':')
    game_id = int(new_line[0].split(' ')[-1])
    rounds = new_line[1].split(';')
    rounds_check = []
    # For part 2
    min_cubes = [0,0,0] # R,G,B
    for round in rounds:
        cubes_sets = round.split(',')
        cubes = [0,0,0] # R,G,B
        for cube in cubes_sets:
            amount, color = cube.strip().split(' ')
            amount = int(amount)
            cubes[convert[color]] += amount
            # Check for part 2
            if amount > min_cubes[convert[color]]:
                min_cubes[convert[color]] = amount
        # Check for part 1
        check = [cubes[x] <= 12+x for x in range(3)]
        rounds_check.append(all(check))
    # Adding part 1 subtotal
    if all(rounds_check):
        total_sum += game_id
    # Adding part 2 subtotal
    power = min_cubes[0] * min_cubes [1] * min_cubes[2]
    total_power += power

print(f"Part one answer: Total sum of valid games ids --> {total_sum}")
print(f"Part two answer: Total sum of cube sets power --> {total_power}")

