def main():
    yell("This", "is", "map", "function")


def yell(*words):
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()