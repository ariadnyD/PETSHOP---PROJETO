import pickle

cachorros = {}
try:
  arq_cachorros = open("cachorros.dat", "rb")
  cachorros = pickle.load(arq_cachorros)
except:
  arq_cachorros = open("cachorros.dat", "wb")
arq_cachorros.close()

servicos = {}
try:
  arq_servicos = open("servicos.dat", "rb")
  servicos = pickle.load(arq_servicos)
except:
  arq_servicos = open("servicos.dat", "wb")
arq_servicos.close()

agenda = {}
try:
  arq_agenda = open("agenda.dat", "rb")
  agenda = pickle.load(arq_agenda)
except:
  arq_agenda = open("agenda.dat", "wb")
arq_agenda.close()

