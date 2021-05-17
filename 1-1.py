def main():
    print(chap1q1("abcdefghijklmnopqrstuvwxyz"))
    print(chap1q1("aabcdefghijklmnopqrstuvwxyz"))


def chap1q1(string):
    # I'm assuming the lower case alphabet as a character set
    alphabet = "00000000000000000000000000"

    for letter in string:
        temp = ""
        # ord('a') acts as the offset for the alphabet string
        if alphabet[ord(letter)-ord('a')] == '1':
            return False
        for i in range(0, len(alphabet)):
            if i == ord(letter)-ord('a'):
                temp += str(1)
            else:
                temp += alphabet[i]
        alphabet = temp
    return True


if __name__ == '__main__':
    main()
