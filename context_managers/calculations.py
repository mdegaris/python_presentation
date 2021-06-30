from decimal import Decimal, localcontext

# Don't want to rely on float.
with localcontext() as ctx:
    ctx.prec = 42
    r1 = Decimal("1") / Decimal("42")
    print ('{}'.format(r1))

r2 = Decimal("1") / Decimal("42")
print ('{}'.format(r2))
