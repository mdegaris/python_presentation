import dis
import typing
from lib.speedtest import *

def add(a: int, b: int) -> int:
    return a + b

def test(f):
    sum = f()
    print("Sum = {s}".format(s=sum))

def main():
    test(slow)
    test(fast)
    test(faster)

    print("******** slow ********")
    dis.dis(slow)
    print("******** fast ********")
    dis.dis(fast)
    print("******** faster ********")
    dis.dis(faster)

if __name__ == "__main__":
    main()