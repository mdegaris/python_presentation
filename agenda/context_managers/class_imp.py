
# Class implementation of a context manager.
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('context_managers/files/test1.txt', 'r') as rfile:
    print(rfile.read())
