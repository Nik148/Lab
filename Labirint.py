from sys import exit
from random import randint
from textwrap import dedent
from os import system


class Figth(object):
	def __init__(self, enemy):
		self.enemy = enemy

	def red(self, enemy):
		# Begin.hp_player - это здоровье игрока, Begin.pw_player - это урон игрока
		hp_opponent = self.enemy[0]
		power_opponent = self.enemy[1]
		# бой идет пока здоровье одного из участников не станет <= 0
		while Begin.hp_player > 0 and hp_opponent > 0:
			storona_at = int(Vvod("Выбери сторону атаки: слева(1) справа(2) сверху(3)\n ",["1", "2", "3"]))

			att_pre = randint(1, 3)
			if storona_at != att_pre:
				hp_opponent = hp_opponent - Begin.pw_player
				print(f"Вы попали! У него осталось {hp_opponent}")
			else:
				print("Он отбил вашу атаку")
			# проверка здоровья после атаки
			if hp_opponent <= 0:
				break
			storona_df = int(Vvod("Выбери сторону защиты: слева(1) справа(2) сверху(3)\n ",["1", "2", "3"]))
			def_pre = randint(1,3)
			if storona_df == def_pre:
				print("ЦццЦинь... Вы отбили атаку")
			else:
				Begin.hp_player = Begin.hp_player - power_opponent
				print(f"Ааааай. Вы пропустили удар. У вас осталось {Begin.hp_player}")
		if Begin.hp_player <= 0:
			dead = [
			"Вы погибли!",
			"Вас разрубили пополам!",
			"Ваша голова слетела с плеч!",
			"Вы пытаетесь собрать свои кишки"
			]
			print(dead[randint(0,3)])
			Dead().read()

		else:
			print("Из этой схватки вы вышли победителем!")
			return 1


class Begin(object):
	hp_player = 0
	pw_player = 0
	def red(self):
		print("""
Вы один из славных воинов Греции приплыли на остров Крит за вечной славой
Но чтобы добыть эту славу, вам нужно зайти в лабиринт, в котором живет сильнейшее из всех творений Посейдона - Минотавр
Вас ждут смертельные ловушки и ужасные монстры. Да прибудет с вами сила!!!
		""")

		ier = Vvod("Для начала вам надо выбрать себе бонусное снаряжение: доспехи Кратоса(1) или меч Персея(2)\n ", ["1", "2"])
		if ier == "1":
			Begin.hp_player = 42
			Begin.pw_player = 5
			
		elif ier == "2":
			Begin.hp_player = 32
			Begin.pw_player = 7

		return Vxod()
		
class Engine(object):
	def __init__(self, map):
		self.map = map

	def play(self):
		scene1 = self.map
		while scene1:
			scene1 = scene1.red()

class Enemy(object):
	opponent = {
	"golem": [25, 2],
	"minotavr": [50, 6], 
	"cerberus": [20, 4], 
	"centaur": [25, 3],
	"chimera": [30, 4]
	}

		

class Dead(object):
	def red(self):
		print("А победа была так близка...")
		system("pause")
		exit(0)

class Vxod(object):
	def red(self):
		print("""
Спустившись в лабиринт, вы оказыватесь в кромешной темноте
Зажгя факел, вы обнаруживаете для себя три прохода
В левом проходе вы слышите журчание воды(1), справа слышите странные звуки(2), лишь проход прямо никак не выделяется(3)
Куда решитесь зайти?
		""")
		a = Vvod("", ["1", "2", "3"])
		if a == "1":
			return Canal()
		elif a == "2":
			return Most()
		else:
			return Sklep()

class Canal(object):
	def red(self):
		print("Пройдя дальше вы видите канал")
		print("Странные крики издаются около воды")
		print("О нет... Это кентавр")
		print("Вы берете меч в руки и начинаете сражение")
		Figth(Enemy().opponent["centaur"]).red(Enemy().opponent["centaur"])
		print("Под водой вы видите странный просвет и решаетесь нырнуть туда")
		print("Плывя под водой вы чувствуете что осталось мало воздуха")
		print("Развернетесь назад(1) или продолжите плыть дальше(2)")
		a = Vvod("", ["1", "2"])
		if a == "1":
			print("Вам не хватило воздуха и вы задохнулись")
			return Dead()
		else:
			print("Наконец то вы нашли выход и выплыли, a ведь воздуха могло не хватить")
			return Gidra()

class Gidra(object):
	def red(self):
		print("Выйдя из воды, вы понимаете, что оказалтсь в пещере")
		print("Откуда ни возьмись появляется гидра с тремя головами")
		print("Какую голову ей отрежете? Правую(1), левую(2) или среднюю(3)")
		print("А может ей отрезать хвост?(4)")
		print("Или ноги?(5)")
		y = Vvod("", ["1", "2", "3", "4", "5"])
		if y == "4":
			print("Гидра замертво упала и больше не вставала. Вы молодец!!!")
			return Final()
		elif y == "5":
			print("Пока вы пытались отрезать ей ногу, гидра оторвала вам голову")
			return Dead()
		else:
			print("На месте этой головы отрасли две новые")
			print("Вас разорвали на кусочки")
			return Dead()

class Final(object):
	def red(self):
		print("Оказавшись в большой комнате, вы видите вдали лестницу, которая выведет вас из лабиринта")
		print("Но перед ней стоит непонятное существо с головой льва и козла и заместо хвоста у нее змея")
		print("Это же Химера!!! Бой будет тяжелым")
		Figth(Enemy().opponent["chimera"]).red(Enemy().opponent["chimera"])
		print("Очень устав, вы продолжаете двигаться к выходу")
		print("И вот она!!! Долгожданная победа!")
		print("Вы стали одним из великих воинов Греции!")
		print("Поздравляю! Вы прошли игру!")
		system("pause")
		exit(0)

class Most(object):
	def red(self):
		print("Пройдя направо, вы выходите на мост, пролегающей над огромной бездной")
		print("Странный звук усиливается и вы видите как на вас бежит цербер")
		print("Придется драться...")
		Figth(Enemy().opponent["cerberus"]).red(Enemy().opponent["cerberus"])
		print("""
Покончив с цербером, вы начинаете осматриваться, и видите, что мост в одном месте частично разрушен
Что будете делать? Перепрыгните этот участок(1) или аккуратно по нему пройдете(2)
		""")
		y = Vvod("", ["1", "2"])
		if y == "1":
			print("С криками: 'ААААААААА' - вы перепрыгиваете опасный участок моста и идете дальше")
			return Velican()
		else:
			print("Мост рушится, вы летите вниз и думаете: 'Когда в своей жизни я свернул не туда???' ")
			return Dead()

class Velican(object):
	def red(self):
		print("Тут есть дверь! Вы заходите туда и видите спящего Циклопа. ОН ОГРОМЕН! ")
		print("Около него лежит какой то ключ! Хотите ли вы его взять?(да-1, нет-2)")
		x = Vvod("", ["1", "2"])
		if x == "1":
			print("Значит надо очень тихо на носочках подкрасться к нему(1). Хотя можно и отвлечь его чем-то(2)")
			y = Vvod("Что будешь делать?\n", ["1", "2"])
			if y == "1":
				print("Огр проснулся и превратил вас в кровавую мессиву!")
				return Dead()
			elif y == "2":
				print("Вы нашли какой то камень и кинули его куда подальше. Огр проснулся и пошел на источник шума")
				print("Быстро взяв ключ, вы побежали к дальше по комнате и увидели люк с замком")
				print("Открыли замок и залезли в люк")
				return Luck()
		elif x == "2":
			print("Пройдясь по комнате дальше, вы нашли люк с замком. Но он не открывается...")
			print("Проснулся огр и съел вас.")
			return Dead()

class Luck(object):
	def red(self):
		print("Здесь так тесно!")
		print("Вы еле еле пролезли дальше и приползли к двум выходам")
		print("На одном выходе табличка с головой льва(1), другая с шипами(2)")
		x = Vvod("Куда пойдете?\n", ["1", "2"])
		if x == "1":
			return Final()
		else:
			return Kapkan()

class Kapkan(object):
	def red(self):
		print("Вы оказываетесь в просторной комнате c шипами на стенах")
		print("О нет!!! Стены начинают сужаться")
		print("Надо что то делать")
		print("Может поробовать открыть люк из которого вы вышли(1), найти скрытую кнопку на стене(2) или на полу(3) ")
		x = Vvod("", ["1", "2", "3"])
		if x == "1":
			print("Вы пытаетесь изо всех сил вырвать люк но его заклинило")
			print("А стены все ближе и ближе...")
			print("Вас растерзало шипами")
			return Dead()
		else:
			print("К сожалению, а может и к счастью, кнопки не оказалось")
			print("Вас прокололи шипы")
			return Dead()

class Sklep(object):
	def red(self):
		print("Оказывается здесь склеп воинов, пытавшихся выбраться из лабиринта. Их так много!")
		print("Вот почему здесь так тихо")
		print("Своими шагами вы пробудили голема, стража этого склепа")
		print("Придется с ним драться")
		Figth(Enemy().opponent["golem"]).red(Enemy().opponent["golem"])
		print("Тело голема превратилось в прах")
		print("Шагая дальше, вы удивляетесь, сколько здесь скелетов славных бойцов")
		print("ААА, вы провалилсь в яму с муравьями-людоедями")
		print("Что будете делать???")
		print("Можно от них отбиться(1), Подняться по хлипкой лестнице(2),")
		print("Подянться по камням(3) или  попытаться открыть непонятный люк на стене(4)")
		x = Vvod("", ["1", "2", "3", "4"])
		if x == "3":
			print("Вы удачно вскарабкались по камням, как скалолаз")
			print("Может вам надо было становиться альпинистом, а не воином")
			return Minotavr()
		elif x == "4":
			print("Открыв люк, вы выдите трубу и прыгаете в неё")
			print("Пролетев в ней пару секунд, вы оказываетесь в неизвестной комнате")
			return Velican()
		elif x == "1":
			print("Их здесь так много! Они лезут со всех щелей")
			print("О НЕТ!!! ОНИ МЕНЯ ЕДЯТ ПО КУСОЧКАМ")
			print("Вас съели жалкие муравьи")
			return Dead()
		else:
			print("Почти добравшись до конца лестницы она падает и вы разбиваетесь")
			return Dead()
		
class Minotavr(object):
	def red(self):
		print("Пройдя дальше вы оказыветесь в сокровищне с большим количеством золота. ВСЕ МОЕ!")
		print("Странные вздохи обрывают вам экстаз")
		print("Перед вами появляется сам король лабиринта - Минотавр")
		print("Понимаю, что этот бой может стать последним, вы принимаете боевую стойку")
		Figth(Enemy().opponent["minotavr"]).red(Enemy().opponent["minotavr"])
		print("Взяв голову минотавра, вы спокойно садитесь и наслаждайетесь проделанным путем")
		print("Теперь вы не только самый великий воин Греции, но и самый богатый")
		system("pause")
		exit(0)



def Vvod(text, spisok):
    while True:
        a = input(text)
        if a not in spisok:
            print("Не ломай игру, введи один из предложенных символов") 
            continue
        return a



x = Engine(Begin())
x.play()
