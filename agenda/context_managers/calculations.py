from decimal import Decimal, localcontext


# Create a context with precision = 42
with localcontext() as ctx:
    ctx.prec = 42
    one = Decimal("1")
    seven = Decimal("7")
    answer1 = one / seven

# Outside context so revert default precision (of 28)
answer2 = one / seven

print
print ('Precision=42:\t\t{}'.format(answer1))
print ('Precision=default(28):\t{}'.format(answer2))
print
