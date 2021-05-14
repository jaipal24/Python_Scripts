# Given a list of numbers, the task is to write a Python program to find the second largest number in given list.
# Example:
# Input: list1 = [10, 20, 4]
# Output: 10
def sec_large(lt1):
    max_val = max(lt1[0], lt1[1])
    sec_max = min(lt1[0], lt1[1])
    for ele in lt1:
        if sec_max < ele < max_val:
            sec_max = ele
        elif max_val < ele:
            sec_max = max_val
            max_val = ele
    return sec_max


if __name__ == "__main__":
    lt = list(map(int, input("Enter list elements:").split(" ")))
    print("2nd Largest element in the list:{0}".format(sec_large(lt)))
