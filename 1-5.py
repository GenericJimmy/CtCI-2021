def main():
    print(chap1q5("feel", "eel"))
    print(chap1q5("feel", "fell"))
    print(chap1q5("feel", "fall"))


def chap1q5(string1, string2):
    if string1 == string2:
        return True
    elif len(string1) == len(string2):
        dict1 = enumerated_dictionary(string1).copy()
        dict2 = enumerated_dictionary(string2).copy()
        return(one_letter_swap(dict1, dict2))
    elif abs(len(string1)-len(string2)) == 1:
        dict1 = enumerated_dictionary(string1).copy()
        dict2 = enumerated_dictionary(string2).copy()
        return(one_insert_or_remove(max(dict1, dict2), min(dict1, dict2)))
    else:
        return False


def enumerated_dictionary(string):
    dict = {}
    for i in range(0, len(string)):
        dict[i] = string[i]
    return(dict)


def one_insert_or_remove(dict_longer, dict_shorter):
    num_differences = 0
    offset = 0
    for key in dict_shorter:
        if (dict_shorter[key] != dict_longer[key + offset]):
            num_differences += 1
            offset += 1
        if num_differences > 1:
            return False
    return True


def one_letter_swap(dict1, dict2):
    num_differences = 0
    for key in dict2:
        if dict1[key] != dict2[key]:
            num_differences += 1
        if num_differences > 1:
            return False
    return True


if __name__ == '__main__':
    main()
