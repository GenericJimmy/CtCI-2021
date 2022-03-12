def main():
    print(chap1q2("leaf", "flea"))
    print(chap1q2("leaf", "leef"))


def chap1q2(string1, string2):
    if len(string1) == len(string2):
        return catalogue(string1) == catalogue(string2)
    return False


def catalogue(string):
    dict = {}
    for letter in string:
        dict[letter] = 0
    for letter in string:
        dict[letter] += 1
    return(dict)


if __name__ == '__main__':
    main()
