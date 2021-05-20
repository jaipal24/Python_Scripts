# Given a string “str” and another string “sub_str”.
# We are allowed to delete “sub_str” from “str” any number of times.
# It is also given that the “sub_str” appears only once at a time.
# The task is to find if “str” can become empty by removing “sub_str” again and again.
def rec_del(st, sub_st):
    if len(st) == 0 and len(sub_st) == 0:
        return "YES"
    if len(sub_st) == 0:
        return "YES"
    while len(st) != 0:
        ind = st.find(sub_st)
        if ind == -1:
            return "NO"
        st = st[0:ind] + st[ind+len(sub_st):]
    return "YES"


if __name__ == "__main__":
    s = input("Enter a string:")
    sub_s = input("Enter substring:")
    print("Can the main string be emptied by continuous deletion of sub string:", rec_del(s, sub_s))
