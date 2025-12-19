def change(lot, nom_1, nom_2, nom_3):
    """
    Первым вргументом является сумма, которую необходимо разменять.
    Остальные 3 аргумента - номиналы, любые ненулевые.
    Функция ищет самый легкий размен.
    """

    all_nom = sorted([nom_1, nom_2, nom_3], reverse=True)

    for count_0 in range(lot // all_nom[0] + 1):
        rest_1 = lot - count_0 * all_nom[0]

        for count_1 in range(rest_1 // all_nom[1] + 1):
            rest_2 = rest_1 - count_1 * all_nom[1]

            if rest_2 % all_nom[2] == 0:
                result = [count_0, count_1, rest_2 // all_nom[2]]
                print(
                    f"размен: {all_nom[0]} * {result[0]} + "
                    f"{all_nom[1]} * {result[1]} + {all_nom[2]} * {result[2]}"
                )
                return

    else:
        print("-42!")
        return

FIO = input("Введите через пробел имя, фамилию и отчество\n").split()
nominals = [len(string) for string in FIO]
if len(nominals) == 2:
    nominals += [19]
lot_to_change = int(input("Введите сумму, которую нужно разменять\n"))
change(lot_to_change, nominals[0], nominals[1], nominals[2])
