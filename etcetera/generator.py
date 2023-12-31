# n = int(input("What's n?: "))

# for i in range(n):
#     print("*" * i)

def main():
    n = int(input("What's n?: "))
    for s in give_life_ram(n):
        print(s)

# kill your RAM :)
# def ram_killer(n):
#     array = []
#     for i in range(n):
#         array.append("*" * i)
#     return array


def give_life_ram(n):
    for i in range(n):
        yield "*" * i
    
if __name__ == "__main__":
    main()
