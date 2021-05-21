# we can have a problem in which we need to flatten dictionary of key-value pair
# pairing the equal index elements together.
# This can have utilities in web development and Data Science domain.
if __name__ == "__main__":
    dt = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
    print("The original dictionary is:", dt)
    res = dict(zip(dt['month'], dt['name']))
    print("After converting into flat dictionary:", res)
