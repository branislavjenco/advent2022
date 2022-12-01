from utils import file_into_list, file_into_string

# part 1
inp = file_into_string("day1/input.txt")
elves = inp.split("\n\n")
calories = [ [int(cal) for cal in elf.split("\n") if cal != ""] for elf in elves]
sums = [ sum(x) for x in calories ]

print("Part 1:", max(sums))

# part 2

print("Part 2:", sum(sorted(sums, reverse=True)[:3]))


