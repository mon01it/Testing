# сделать проверу всего алгоритма, сложив все компоненты и сравнив их с переменной cash
# +++ограничить в принтах вывод до сотых
# позволить вводить в инпутах данные с любый количеством чисел после запятой, не использую саму запятую
# сделать защиту от ввода неверных данных, символов, букв и пробелов
# сделать возможность глобального подсчета, с нужноц корректировкой в определенную сторону. или автономный ввод, независящий от уже накопленного
# число выводов не может быть отрицательным, как при вводи cashif   авным 10
# +++ и не должно быть, что  вывод юсд 0, а еур больше 0. так как юсд в приоритете
# при малом cash, когда есть юсд и бай, а евро нет, переходить на другой алгоритм не кратно 5, а кратно 1 в евро,
# а бай уменьшать до 0. так как в приоритете купить валюту, а не сохранить в бай
# дать возможность вводить как с запятой, так и без
# создать функцию def и использовать для тренировки навыка
# сделать лимит, после которого не откладывать бай
# так как инпутов много, делать один ввод для этого меню
# +++зациклить
# если введен один 0 то на следующей этерации предлагать ввести только его, а на следующей ничего не предлагать
#сделать зависимость от оконания (рубля, рублей)

x = 0  # счетчик циклов
main_eur = 0  # количество EUR

while True:
    """ФУНКЦИЯ ВВОДА ДАННЫХ И ИХ ПРОВЕРКИ"""
    def control_input(text, vid, text_two, text_tree):
        name = input(text)
        while True:
            try:
                name_two = vid(name)
                if name_two == 0:
                    print(text_tree)
                    break
                elif name_two < 0:
                    name = input("Число не может быть отрицательным\n" + text)
                else:
                    name_two = int(name_two)
                    print(name_two, "рубля.")
                    break
            except ValueError:
                name = input(text_two + text)
        return name_two


    # сбор данных
    while True:
        cash = control_input("Введи сумму предполагаемых инвестиций\n", float, "Это не число\n", "Нельзя инвестировать 0 рублей")
        if cash > 0:
            break
    a = "Это не число\n"
    b = "Не учитывается\n"
    if x == 0:
        usd_index = control_input("Курс USD\n", float, a, b)
        eur_index = control_input("Курс EUR\n", float, a, b)
    elif usd_index > 0 and eur_index == 0:
        eur_index = control_input("Курс EUR\n", float, a, b)
    elif eur_index > 0 and usd_index == 0:
        usd_index = control_input("Курс USD\n", float, a, b)


    # алгоритм определения размера поступления
    if cash > 100:
        a, b = 40, 30
    elif cash > 50:
        a, b = 45, 20
    else:
        a, b = 50, 10

    # алгоритм usd
    if usd_index > 0 and eur_index > 0:  # Если ввел USD/EUR
        main_usd = (cash / 100 * a) // usd_index
        if main_usd % 5 >= 3:
            main_usd = (main_usd // 5 * 5) + 5
        else:
            main_usd = main_usd // 5 * 5
        if main_usd != 0:
            print("Выйдет:", main_usd, "USD")
    elif eur_index > 0:  # если ввел только EUR
        usd_index = 0
        main_usd = 0

    # если ввел только USD
    else:
        if cash < 30:
            main_usd = (cash / 100 * (100 - b)) // usd_index
        else:
            main_usd = (cash / 100 * a) // usd_index
            if main_usd % 5 >= 3:
                main_usd = (main_usd // 5 * 5) + 5
            else:
                main_usd = main_usd // 5 * 5
        print("\nВыйдет", main_usd, "USD")

    # алгоритм EUR
    if usd_index > 0 and eur_index > 0:  # если ввел USD/EUR
        main_eur = ((cash - (cash / 100 * (a + b))) - (main_usd * usd_index)) // eur_index
        if main_eur % 5 >= 3.5:
            main_eur = main_eur // 5 * 5 + 5
        if cash - (main_usd * usd_index) - (main_eur * eur_index) < 0:
            main_eur -= 5
        else:
            main_eur = main_eur // 5 * 5
        if main_eur != 0:
            print("Выйдет в EUR:", main_eur)
    elif eur_index > 0:  # если ввел только EUR
        main_eur = cash // eur_index
        if main_eur > 0:
            print("Выйдет в EUR:", main_eur)

        # алгоритм byn
    if usd_index > 0 and eur_index > 0:
        main_byn = cash - (main_usd * usd_index) - (main_eur * eur_index)
        a = main_byn
        main_byn = main_byn // 5 * 5
        if main_byn != 0:
            print("Отложить в BYN:", "%.2f" % main_byn)

        # алгоритм остатка
        if usd_index > 0 and eur_index > 0:
            main_ost = (usd_index * main_usd) - (eur_index * main_eur) - main_byn
        else:
            main_ost = cash - (usd_index * main_usd) - (eur_index * main_eur)
        if main_ost > 0:
            print("Сумма остатка:", "%.2f" % main_ost)
        else:
            print("Ошибка")
        print("\n=====================\n\n")
    x += 1