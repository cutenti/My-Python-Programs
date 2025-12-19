def reverse_compare(str_1, str_2):
    len_1 = len(str_1)
    len_2 = len(str_2)

    for i in range(min(len_1, len_2)):
        if str_1[i] > str_2[i]:
            return 2  # str_2 > str_1
        if str_2[i] > str_1[i]:
            return 1  # str_1 > str_2

    if len_1 > len_2:
        return 1

    if len_2 > len_1:
        return 2

    return 0  # str_1 == str_2
