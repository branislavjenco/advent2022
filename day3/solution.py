from utils import file_into_list

rucksacks = [ (ruck[:(len(ruck)//2)], ruck[(len(ruck)//2):]) for ruck in file_into_list("day3/input.txt")]

def priority(ch):
    if 96 < ord(ch) < 123:
        return ord(ch) - 96
    else:
        return ord(ch) - 38

s = sum([ priority((set(list(a)) & set(list(b))).pop()) for a, b in rucksacks])
print("Part 1: ", s)
