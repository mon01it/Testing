cash = 100
if cash > 100:
    a, b, c = 40, 30, 30
elif cash > 50:
    a, b, c = 45, 35, 20
else:
    a, b, c = 50, 40, 10
usd_index = 2
eur_index = 3
def algoritm (index, index_two, letter):
    if index > 0 and index_two > 0:
        main = (cash / 100 * letter) // index
        if main % 5 >= 3:
            main = (main // 5 * 5) + 5
        else:
            main = main // 5 * 5
    elif index > 0
