# --- Day 1: Trebuchet?! ---

# Part one 
with open('input01.txt') as f:
    lines = f.readlines()

values = []
for line in lines:
    numbers = [x for x in line if x.isdigit()]
    cal_value = int(numbers[0] + numbers[-1])
    values.append(cal_value)

print(f"Part one answer - Calibration value sum: {sum(values)}")

# Part two
values = []
nums = {"one": "1", "two": "2","three": "3","four": "4", "five": "5",
         "six": "6", "seven": "7","eight": "8", "nine": "9",}

def find_nums_in_line(data_line, nums_dict):
    first = ""
    for i in range(len(data_line)):
        if data_line[i].isdigit():
            first = data_line[i]
            break
        else:
            try:
                three,four,five = data_line[i:i+3],data_line[i:i+4],data_line[i:i+5]
            except IndexError:
                print("Index out of line")
            if three in nums_dict:
                first = nums_dict[three]
                break
            elif four in nums_dict:
                first = nums_dict[four]
                break
            elif five in nums_dict:
                first = nums_dict[five]
                break
    last = ""
    for i in range(len(data_line)-1, -1, -1):
        if data_line[i].isdigit():
            last = data_line[i]
            break
        else:
            try:
                three,four,five = data_line[i-2:i+1],data_line[i-3:i+1],data_line[i-4:i+1]
            except IndexError:
                print("Index out of line")
            if three in nums_dict:
                last = nums_dict[three]
                break
            elif four in nums_dict:
                last = nums_dict[four]
                break
            elif five in nums_dict:
                last = nums_dict[five]
                break
    return int(first+last)

for line in lines:
    values.append(find_nums_in_line(line, nums))

print(f"Part two answer - Calibration value sum: {sum(values)}")
   