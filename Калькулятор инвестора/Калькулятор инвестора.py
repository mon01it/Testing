# +++сделать проверу всего алгоритма, сложив все компоненты и сравнив их с переменной cash
# +++ограничить в принтах вывод до сотых
# +++позволить вводить в инпутах данные с любый количеством чисел после запятой, не использую саму запятую
# +++сделать защиту от ввода неверных данных, символов, букв и пробелов
# +++сделать возможность глобального подсчета, с нужноц корректировкой в определенную сторону. или автономный ввод, независящий от уже накопленного
# +++число выводов не может быть отрицательным, как при вводи cashif   авным 10
# +++ и не должно быть, что  вывод юсд 0, а еур больше 0. так как юсд в приоритете
# +++при малом cash, когда есть юсд и бай, а евро нет, переходить на другой алгоритм не кратно 5, а кратно 1 в евро,
# +++а бай уменьшать до 0. так как в приоритете купить валюту, а не сохранить в бай
# +++дать возможность вводить как с запятой, так и без
# +++ создать функцию def и использовать для тренировки навыка
# сделать лимит, после которого не откладывать бай
# так как инпутов много, делать один ввод для этого меню
# +++зациклить
# +++если введен один 0 то на следующей этерации предлагать ввести только его, а на следующей ничего не предлагать
# сделать зависимость от оконания (рубля, рублей)

loops = 0 #счетчик циклов
while True:
	flag = False #выход из вложенных циклов

	'''___ФУНКЦИЯ ПОДБОРА ОКОНЧАНИЯ РУБЛЕЙ___(работает только с целыми числами'''
	def endigs(index):
		a1, a2, a3, a4 = 'рубль\n', 'рубля\n', 'рублей\n', '--------'
		while True:
			if index < 5:
				if index == 0:
					name = a3 + a4
				elif index % 4 == 0:
					name = a2 + a4
				elif index % 3 == 0:
					name = a2 + a4
				elif index % 2 == 0:
					name = a2 + a4
				else:
					name = a1 + a4
				break
			elif 5 <= index <= 20:
				name = a3 + a4
			else:
				index = index % 10
				continue
			break
		return name

	"""ФУНКЦИЯ ВВОДА ДАННЫХ И ИХ ПРОВЕРКИ"""
	def control_input(flag_two, text, typer, text_two, text_tree):
		"""ФУНКЦИЯ ПРИВЕДЕНИЯ ЦЕЛОГО ЧИСЛА КУРСА В ВЕЩЕСТВЕННОЕ"""
		def index_float(z):
			if z[1] != '.':
				z = z.replace('.', '').replace(',', '')
			z = z[0], '.', z[1:]
			z = str(z)[1:-1].replace(', ', '').replace("'", '')
			return z
		name = input(text)
		while True:
			try:
				name_two = typer(name)
				if name_two == 0:
					print(text_tree)
					break
				elif name_two < 0:
					name = input("Число не может быть отрицательным\n_________________________________\n\n" + text)
				elif flag_two == 0:
					name_two = typer(name_two)
					print(name_two, endigs(name_two))#вывод если все правильно
					break
				else:
					name_two = index_float(str(name_two))
					print(name_two)
					break
			except ValueError:
				name = input(text_two + text)
		return typer(name_two)
	# сбор данных
	while True:
		cash = control_input(0, "Введи сумму предполагаемых инвестиций\n", int, "Это не число\n____________\n\n",
							 "Нельзя инвестировать 0 рублей")
		if cash > 0:
			break
		elif cash == 0 and loops > 0:
			flag = True
			break
	if flag:
		loops = 0
		print(loops)
		continue
	a, b = "Это не число\n", "Не учитывается\n"
	if loops == 0:
		usd_index = control_input(1, "Курс USD\n", float, a, b)
		eur_index = control_input(1, "Курс EUR\n", float, a, b)
	elif usd_index > 0 == eur_index and loops < 2:
		eur_index = control_input("Курс EUR\n", float, a, b)
	elif eur_index > 0 and usd_index == 0 and loops < 2:
		usd_index = control_input("Курс USD\n", float, a, b)

	# алгоритм определения размера поступления
	if cash > 100:
		a, b, c = 40, 30, 30
	elif cash > 50:
		a, b, c = 45, 35, 20
	else:
		a, b, c = 50, 40, 10

	"""ФУНКЦИЯ ПРИВЕДЕНИЯ ОСТАТКА КРАТНОМУ ПЯТИ"""
	def algo_in(price, cash_one, main):
		if cash_one >= price:
			if main % 5 >= 3:
				main = (main // 5 * 5) + 5
			else:
				main = main // 5 * 5
		return main

	"""ОСНОВНОЙ АЛГОРИТМ"""
	def algoritm(index, index_two, letter, letter_two):
		if index > 0 and index_two > 0:
			main = cash / 100 * letter // index
			main = algo_in(40, cash, main)
		elif index > 0:
			main = cash / 100 * (letter + letter_two) // index
			main = algo_in(30, cash, main)
			if cash < (main * index):
				main -= 5
		else:
			main = 0
		return main

	"""ФУНКЦИЯ ВЫВОДА ЕСЛИ >0"""
	def print_out(main, simple_index):
		if main != 0:
			print(main, simple_index)

	# вычисление USD
	main_usd = algoritm(usd_index, eur_index, a, b)
	print_out(main_usd, "usd")

	# вычисление EUR
	main_eur = algoritm(eur_index, usd_index, b, a)
	print_out(main_eur, "eur")

	# вычисление BYN
	main_byn = cash - (usd_index * main_usd) - (eur_index * main_eur)
	main_byn = algo_in(50, cash, main_byn)
	if cash - (usd_index * main_usd) - (eur_index * main_eur) - main_byn < 0:
		main_byn -= 5
	if main_byn // 5 > 0:
		main_byn = main_byn // 5 * 5
	main_byn //= 1 * 1
	print_out(main_byn, "BYN")

	# вычисление остатка
	main_ost = cash - (usd_index * main_usd) - (eur_index * main_eur) - main_byn
	if main_ost >= 0:
		print("Сумма остатка:", "%.2f" % main_ost, "рубля")
	else:
		print("Ошибка")
	print("\n=====================\n\n")
	loops += 1