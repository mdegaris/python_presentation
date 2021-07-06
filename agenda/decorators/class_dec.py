# Python program showing
# use of __call__() method

class MyDecorator:
    def __init__(self, function):
        print("__init__")
        self.function = function

    @staticmethod
    def __call__(self):

        print("__call__")

        # We can add some code
        # before function call

        self.function()

        # We can also add some code
        # after function call.


# adding class decorator to the function
@MyDecorator
def function():
    print("GeeksforGeeks")


function()
