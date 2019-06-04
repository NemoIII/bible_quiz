import csv, sys
from random import choice
# import path

'''Tentando me lembrar de como coloco o path, ainda pesquisando algo satisfatório.'''

q = [] ''' não tenho certeza do que eu fiz nessa linha, a idéia é criar uma lista vazia para armazenar a questão selecionada na class Play. Ainda definindo como será.'''

a = [] ''' e nem nessa. Coloquei aqui para futuras referências e a idéia é a mesma de cima. '''

res = []

class Play():
	def open_quest():
	'''quest = open("questions.csv", "r")
	reader = csv.reader(quest) 
	for line in reader:
	    print linha
    Pode ser feito como o exemplo acima''' 
		with open("questions.csv", "r") as quest:
			reader = csv.reader(quest)
 			q = random.choice(quest.readline())
	 	'''try:
 			for (variable) in reader:
 				q.append(line)
 				# print(q)
	 	except csv.Error as e:
 			sys.exit("quest %s, line %d: %s" % *(quest, reader.line_num, e))'''
			
	def open_answer():
		with open("answer.csv", "r") as an:
			rdr = csv.reader(an)
		try:
			if q is in an:
				res = [q + a]
				return res '''Essa def toda tem que ser mexido, pq ainda não consegui definir como apresentar o join da pergunta com a resposta. Mas a forma de facilitar é, no arquivo de pergunta e de resposta, ex.: Questão 1 (em ambos os arquivos)''' 
		except res is null as e:
			sys.exit("The answer is null!")




quest.close()
an.close()
q.clear()
