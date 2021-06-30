

def dict_comprehensions():

    dict = {"HUMAN": 1,
            "Rat": 2,
            "mouse": 3,
            "guinea Pig": 4}

    squared_values = {k: v ** 2 for (k, v) in dict.items() if v > 2}
    lowercase_keys = {k.lower(): v for (k, v) in dict.items()}

    print("Original dictionary:\t\t{}".format(dict))
    print("Squared value dictionary:\t{}".format(squared_values))
    print("Lowercase keys dictionary:\t{}".format(lowercase_keys))


def main():

    print("\n***** Dictionary Comprehensions ******\n")
    dict_comprehensions()


main()
