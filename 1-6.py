def main():
    print(chap1q6("bell"))
    print(chap1q6("belll"))
    print(chap1q6("bellll"))
    print(chap1q6("belllll"))
    print(chap1q6("bbeeellllll"))


def chap1q6(string):
    compressed_string = []
    inflatable_space = 0
    compressable_space = 0

    i = 0
    while i <= len(string):
        if i+1 < len(string):
            if string[i] != string[i+1]:
                inflatable_space += 1
            elif string[i] == string[i+1]:
                consecutives = count_consecutive(string, i, 0)
                compressable_space += consecutives - len(str(consecutives+1))
                i += consecutives
        if i+1 == len(string):
            if string[i] != string[i-1]:
                inflatable_space += 1
        i += 1

    if inflatable_space >= compressable_space:
        return(string)
    else:

        i = 0
        while i <= len(string):
            if i+1 < len(string):
                if string[i] != string[i + 1]:
                    compressed_string.append(string[i])
                    compressed_string.append(str(1))
                elif string[i] == string[i + 1]:
                    consecutives = count_consecutive(string, i, 0)
                    compressed_string.append(string[i])
                    compressed_string.append(str(consecutives + 1))
                    i += consecutives
            if i + 1 == len(string):
                if string[i] != string[i - 1]:
                    compressed_string.append(string[i])
                    compressed_string.append(str(1))
            i += 1
        return(''.join(compressed_string))


def count_consecutive(string, index, count):
    if index + 1 < len(string) and string[index] == string[index + 1]:
        return(count_consecutive(string, index + 1, count + 1))
    return(count)


if __name__ == '__main__':
    main()
