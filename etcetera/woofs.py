# def woof(n:int):
#     for _ in range(n):
#         print("woof")

# num: int = int(input("Number: "))

# woof(num)

def woof(n:int) -> str:
    return "woof\n" * n

num: int = int(input("Number: "))
woofs: str = woof(num)

print(woofs, end="")