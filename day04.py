# --- Day 3: Gear Ratios ---

with open('input04.txt') as f:
    lines = f.readlines()

# Part one
points = 0
cards = []
for line in lines:
    nums = line.strip().replace('  ', ' ').split(':')[1].split('|')
    winners = set(int(x) for x in nums[0].strip().split(' '))
    card_nums = set(int(x) for x in nums[1].strip().split(' '))
    matches = winners & card_nums
    matches_count = len(matches)
    if matches_count != 0:
        points += 2** (matches_count - 1)

    # For part two
    card_id = int(line.strip().split(':')[0].split(' ')[-1])
    # schema (card_id, qty_matches, card_qty)
    cards.append([card_id, len(matches), 1])
print(f"Part one answer: Total points --> {points}")

# Part two
for card in cards:
    win = card[1]
    card_index = card[0] - 1
    if win > 0:
        for i in range(win):
            cards[card_index + i + 1][2] += card[2]
total_cards = sum(x[2] for x in cards)
print(f"Part two answer: Total cards --> {total_cards}")