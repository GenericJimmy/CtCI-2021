def main():
    print(chap1q4("Never odd or even"))
    print(chap1q4("Never or odd even"))
    print(chap1q4("eevvr doNr odn ee"))


def chap1q4(string):
    dict = {}
    flag = 0

    dict = catalogue(''.join(string.split()).lower()).copy()
    for key in dict:
        if not dict[key] % 2 == 0:
            flag += 1
        if flag > 1:
            return False
    return True


def catalogue(string):
    dict = {}
    for letter in string:
        dict[letter] = 0
    for letter in string:
        dict[letter] += 1
    return(dict)


if __name__ == '__main__':
    main()
