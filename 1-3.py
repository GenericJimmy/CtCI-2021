def main():
    print(chap1q3("do you mr jones      ", 15))


def chap1q3(string, truelength):
    temp = list(string)
    offset = 0

    for i, char in enumerate(temp):
        if temp[truelength - i - 1] != " ":
            temp[len(string) - i - 1 - offset] = temp[truelength - i - 1]
        else:
            temp[len(string) - i - 1 - offset] = "0"
            temp[len(string) - i - 2 - offset] = "2"
            temp[len(string) - i - 3 - offset] = "%"
            offset += 2
    return(''.join(temp))


if __name__ == '__main__':
    main()
