def __del__(self):
    print("==================")
    print("out of scope close")
    print("==================")
    self.file_obj.close()


def open_file(filename):
    File(filename, 'r')


open_file('context_managers/files/test1.txt')
