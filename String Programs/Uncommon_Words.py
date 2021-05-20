# Given two sentences as strings A and B. The task is to return a list of all uncommon words.
# A word is uncommon if it appears exactly once in any one of the sentences,
# and does not appear in the other sentence.
# Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.
def uncommon(st1, st2):
    lt1 = st1.split()
    lt2 = st2.split()
    res = []
    for ele in lt1:
        if ele not in lt2:
            res.append(ele)
    for ele in lt2:
        if ele not in lt1:
            res.append(ele)
    # res = set(lt1).symmetric_difference(set(lt2)) this is another way to find uncommon words.
    return res


if __name__ == "__main__":
    s1 = input("Enter first sentence:")
    s2 = input("Enter second sentence:")
    print("The uncommon words are:", uncommon(s1, s2))
