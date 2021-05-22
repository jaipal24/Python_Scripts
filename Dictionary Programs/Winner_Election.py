# Given an array of names of candidates in an election.
# A candidate name in the array represents a vote cast to the candidate.
# Print the name of candidates received Max vote.
# If there is tie, print a lexicographically smaller name.
from collections import Counter


def winner(dt):
    temp = dict(Counter(dt))
    mx = max(temp.values())
    val = []
    for key, value in temp.items():
        if mx == value:
            val.append(key)
    val.sort()
    return val[0]


if __name__ == "__main__":
    votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
    res = winner(votes)
    print("The winner in the election is:", res)
