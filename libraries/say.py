import cowsay
import sys

# cowsay.tux('Hello World')

if len(sys.argv) == 2:
    cowsay.tux("Hello, " + sys.argv[1])

