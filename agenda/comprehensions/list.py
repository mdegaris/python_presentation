def list_comprehensions():

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    greater5 = [n for n in list if n > 5]
    double_evens = [n * 2 for n in list if n % 2 == 0]

    print("Original list:\t\t{}".format(list))
    print(">5 list:\t\t{}".format(greater5))
    print("Double evens list:\t{}".format(double_evens))


def main():

    print("\n***** List Comprehensions ******\n")
    list_comprehensions()


main()
