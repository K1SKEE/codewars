'''
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many
years he will be twice as old).
Подсчитайте, сколько лет назад отец был вдвое старше своего сына (или через сколько
лет он будет вдвое старше).
'''

def twice_as_old(dad_years_old, son_years_old):
	if dad_years_old < son_years_old * 2:
		print(son_years_old * 2 - dad_years_old)
		return son_years_old * 2 - dad_years_old
	else:
		print(dad_years_old - (son_years_old * 2))
		return dad_years_old - (son_years_old * 2)

twice_as_old(36,7)
twice_as_old(55,30)
twice_as_old(42,21)
twice_as_old(22,1)
twice_as_old(29,0)