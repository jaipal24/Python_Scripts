# The problem statement asks to produce a new list whose
# i^{th} element will be equal to the sum of the (i + 1) elements.
# Examples :
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]
def cum_sum(lt1):
    val = list()
    val.append(lt1[0])
    for i in range(1, len(lt1)):
        val.append(val[i-1]+lt1[i])
    return val


if __name__ == "__main__":
    lt = list(map(int, input("Enter values into list:").split(" ")))
    print("Cumulative sum:", cum_sum(lt))
