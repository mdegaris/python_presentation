from lib.colours import colours

__all__ = ["colour_text"]

# Colours wrapper


# def colour_text(col_prefix):
#     def _wrapper(text):
#         return "{}{}{}".format(col_prefix, text, colours.WHITE)

#     return _wrapper


def tally():
    total = 0

    def _wrapper(n):
        t = total + n
        return (t)
    return _wrapper


t = tally()
print(t(2))
print(t(3))

# green_text = decorate_text(colours.GREEN)
# blue_text = decorate_text(colours.UNDERLINE)

# print(green_text("GREEN"))
# print(blue_text("BLUE"))
