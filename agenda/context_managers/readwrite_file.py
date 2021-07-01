

# File context manager; Read and write
with open("context_managers/files/test1.txt", "r") as rfile, \
        open("context_managers/files/test2.txt", "w") as wfile:

    for number in rfile:
        double_str = str(int(number) * 2)
        wfile.write('{}{}'.format(double_str, '\n'))


print ("Done")
