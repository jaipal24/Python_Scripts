# This program demonstrates how we can sort a list of dictionaries.
from operator import itemgetter
if __name__ == "__main__":
    lt = [{"name": "Nandini", "age": 20}, {"name": "Manjeet", "age": 20}, {"name": "Nikhil", "age": 19}]
    print("Sorting the list by age:")
    print(sorted(lt, key=itemgetter('age')))
    # print(sorted(lt, key=lambda i: i['age'])) we can also use lambda for this process.
    print("Sorting based on both age and name:")
    print(sorted(lt, key=itemgetter('age', 'name')))
    # print(sorted(lt, key=lambda i: (i['age'], i['name']))) we can also use lambda for this process.
