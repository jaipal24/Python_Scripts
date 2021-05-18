# Given a string. The task is to print all words with even length in the given string.
def even_words(str1):
    lt = str1.split(" ")
    val = []
    for ele in lt:
        if len(ele) % 2 == 0:
            val.append(ele)
    return val


if __name__ == "__main__":
    s = input("Enter a string:")
    res = even_words(s)
    print("The even length work in the given string are:")
    for r in res:
        print(r)
