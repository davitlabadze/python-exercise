# def woof(n:int):
#     for _ in range(n):
#         print("woof")

# num: int = int(input("Number: "))

# woof(num)



def woof(n:int) -> str:
    return "woof\n" * n

    """
    Woof N Times.

    :param n: Number of times to woof
    :type n: int
    :raise ValueError: if n in not an int
    :return: A string of n woofs, one per line
    :rtype: str
    """

num: int = int(input("Number: "))
woofs: str = woof(num)

print(woofs, end="")