from lib.colours import colours

__all__ = ["colour_text"]

# Colours wrapper
def colour_text(col_prefix):
    def _wrapper(text):
        return "{}{}{}".format(col_prefix, text, colours.WHITE)

    return _wrapper


# green_text = decorate_text(colours.GREEN)
# blue_text = decorate_text(colours.UNDERLINE)

# print(green_text("GREEN"))
# print(blue_text("BLUE"))
