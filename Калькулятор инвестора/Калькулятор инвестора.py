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

x = 0  # счетчик циклов
main_eur = 0  # количество EUR
while True:  # сбор данных


    """ФУНКЦИЯ ВВОДА ДАННЫХ И ИХ ПРОВЕРКИ"""
    def control_input(name_1, vid,  text_1):
        while True:
            try:
                name = vid(name_1)
                break
            except ValueError:
                name_1 = input(text_1)
            return name



    cash_in = input("Сколько планируется отложить в рублях:\n")



    while True:
        try:
            cash = int(cash_in)
            break
        except ValueError:
            cash_in = input("Это не целое число, попробуйте еще раз.\n")
    # if x == 0:


    """ФУНКЦИЯ ВВОДА КУРСОВ"""
    def input_index(text):
        function = float(input("Курс " + text + " без запятых (с сотыми)\n")) / 100
        if function > 0:
            print(function, "рубля за 1 ", text)
        else:
            print("не учитывается")
        return function


    usd_index = input_index("USD")
    eur_index = input_index("EUR")

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
        if main_usd == 0 or eur_index == 0:
            x -= 1