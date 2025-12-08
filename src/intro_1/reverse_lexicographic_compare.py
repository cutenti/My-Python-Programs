def reverse_compare(str_1, str_2):
    rev_str_1 = str_1[::-1]
    rev_str_2 = str_2[::-1]
    len_1 = len(str_1)
    len_2 = len(str_2)
    for i in range(min(len_1, len_2)):
        if rev_str_1[i] > rev_str_2[i]:
            print(f"строка {str_1} > строки {str_2}")
            return
        if rev_str_2[i] > rev_str_1[i]:
            print(f"строка {str_1} < строки {str_2}")
            return
    if len_1 == len_2:
        print(f"строка {str_1} = строке {str_2}")
        return
    if len_1 > len_2:
        print(f"строка {str_1} > строки {str_2}")
        return
    if len_2 > len_1:
        print(f"строка {str_1} < строки {str_2}")
        return

