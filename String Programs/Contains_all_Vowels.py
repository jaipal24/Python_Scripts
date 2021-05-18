# Given a string, the task is to check if every vowel is present or not.
# We consider a vowel to be present if it is present in upper case or lower case.
# i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .
def contain_vowel(str1):
    str1 = str1.lower().replace(" ", "")
    vowels = set("aeiou")
    res = set({})
    for ch in str1:
        if ch in vowels:
            res.add(ch)
        else:
            pass
    if len(res) == len(vowels):
        return "Accepted"
    else:
        return "Not Accepted"
    # if len(set(string.lower().replace(" ", "")).intersection("aeiou")) >= 5:
    #         return ('accepted')
    # else:
    #         return ("not accepted")
    # This can also get us the same result


if __name__ == "__main__":
    s = input("Enter a string")
    print("Checking all vowels present in given string:", contain_vowel(s))
