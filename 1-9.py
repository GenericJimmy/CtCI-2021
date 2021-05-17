def main():
    print(chap1q9("permutation", "mutationper"))


def chap1q9(string1, string2):
    return(string2 in (string1 + string1))


if __name__ == "__main__":
    main()
