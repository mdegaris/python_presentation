

# File context manager; Read and write
with open("agenda/context_managers/files/test1.txt", "r") as rfile, \
        open("agenda/context_managers/files/test2.txt", "w") as wfile:

    for word in rfile.read().splitlines():
        l = len(word)
        wfile.write('{},{}\n'.format(word, str(l)))


print ("Done")
