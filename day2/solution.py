from utils import file_into_list
from dataclasses import dataclass

strat = file_into_list("day2/input.txt")
test_input = ["A Y", "B X", "C Z"]

op_map = {
        "A": "R",
        "B": "P",
        "C": "S"
        }

me_map = {
        "X": "R",
        "Y": "P",
        "Z": "S"
        }

scores = {
        "R": 1,
        "P": 2,
        "S": 3
        }

@dataclass
class Round:
    op: str
    me: str


def get_outcome(r: Round):
    if (r.me == "R" and r.op == "S") or (r.me == "S" and r.op == "P") or (r.me == "P" and r.op == "R"):
        return 6
    if r.me == r.op:
        return 3
    else:
        return 0


def get_round_score(r: Round):
    outcome = get_outcome(r)
    return scores[r.me] + outcome


rounds = []
for line in test_input:
    parts = line.split(" ")
    r = Round(op_map[parts[0]], me_map[parts[1]])
    rounds.append(r)

print("Part 1: ", sum([get_round_score(r) for r in rounds]))

outcomes = {
        "X": 0,
        "Y": 3,
        "Z": 6
        }

rounds = []
for line in strat:
    parts = line.split(" ")
    r = Round(op_map[parts[0]], parts[1])
    rounds.append(r)

# in part two, the Round.me is the desired outcome of the round
def get_shape(r: Round):
    if r.me == "Y":
        # draw
        return r.op 
    if r.me == "X":
        # lose
        if r.op == "R": return "S"
        if r.op == "S": return "P"
        if r.op == "P": return "R"
    if r.me == "Z":
        # win
        if r.op == "R": return "P"
        if r.op == "S": return "R"
        if r.op == "P": return "S"
print("Part 2: ", sum([scores[get_shape(r)] + outcomes[r.me] for r in rounds]))



