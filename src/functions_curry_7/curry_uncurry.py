def curry(func, arity):
    """
    Каррирование функции с заданной арностью.

    Args:    func - исходная функция,
             arity - арность функции (кол-во ожид. аргументов).

    return: рекурсивно с пустого кортежа собираем все аргументы
            и вызываем для них исходную функцию. Её результат возвращаем.

    raises: ValueError - если арность отрицательная.
    """

    actual_argcount = func.__code__.co_argcount

    if arity > actual_argcount:
        raise ValueError(f"Арность {arity} превышает количество параметров функции")

    if arity < 0:
        raise ValueError("Арность не должна быть <0")

    def curried(args_received):
        """
        Рекурсивная функция, которая копит аргументы.

        args_received: type - tuple, уже полученные аргументы

        return: если все аргументы получены - результат данной функции,
                иначе - новая функция, ждущая след. аргумент.
        """
        if len(args_received) == arity:
            return func(*args_received)

        def next_arg(arg):
            """
            Функция, в которой мы получаем новый аргумент
            и добавлем его к кортежу полученных аргументов.

            return: curried(аргументы + новый) и проверяем,
            достаточно ли аргументов для подсчета результата.
            """
            new_args = args_received + (arg,)
            return curried(new_args)

        return next_arg

    if arity == 0:
        return lambda: func()

    return curried(())


def uncurry(curried_func, arity):
    """
    Функция декаррирования каррированной функции с заданной арностью.

    Args:    curried_func - каррированная функция,
             arity - арность функции.

    return: внутренняя декаррирующая функция, принимающая все аргументы в виде кортежа.

    raise: ValueError - если передана отрицательная арность.
    """
    if arity < 0:
        raise ValueError("Арность не должна быть <0")

    def uncurried(*args):
        """
        Функция, принимающая все аргументы сразу.

        *args - все аргументы функции.

        return: последовательно применяем все аргументы к каррированной
        функции и возвращаем результат.

        raise: TypeError при неверном кол-ве аргументов.
        """
        if len(args) != arity:
            raise TypeError(f"Функция ожидает {arity} аргументов, получено {len(args)}")

        result = curried_func
        for arg in args:
            result = result(arg)

        if arity == 0:
            return result()

        return result

    return uncurried
