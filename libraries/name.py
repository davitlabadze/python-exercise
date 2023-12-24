import sys

# one argument

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")


# few arguments

if len(sys.argv) < 2:
    sys.exit("Too many arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)