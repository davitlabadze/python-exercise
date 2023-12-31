
# python3 chirps.py -n 2
# import sys

# if len(sys.argv) == 1:
#     print("chirp")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("chirp")
# else:
#     print("usage: chirps.py")

import argparse

parser = argparse.ArgumentParser(description="chirp like a bird")
parser.add_argument("-n",default=1,type=int,help="number of times to chirp")
args = parser.parse_args()

for _ in range(args.n):
    print("chirp")