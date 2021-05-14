# Python program to reverse the elements of in a list
# Reversing a list using reversed()
def use_reversed(lt1):
    return [val for val in reversed(lt1)]


# Reversing a list using reverse()
def use_reverse(lt2):
    lt2.reverse()
    return lt2


# Reversing a list using slicing technique
def use_slicing(lt3):
    new_lt = lt3[::-1]
    return new_lt


if __name__ == "__main__":
    lt = list([2, 9, 8, 3, 7])
    print("Using built in reversed function", use_reversed(lt))
    print("Using slicing process:", use_slicing(lt))
    print("Using built in reverse function", use_reverse(lt))
