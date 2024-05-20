import os
import pickle
from dicionarios import cachorros, servicos, agenda

## MENUS
def menu_principal():
  os.system('clear')
  print("############################################")
  print("######     Projeto Miumiu-PetShop     ######")
  print("############################################")
  print("#####     1 - Módulo Cadastrar         #####")
  print("#####     2 - Módulo Pesquisar         #####")
  print("#####     3 - Módulo Atualizar         #####")
  print("#####     4 - Módulo Deletar           #####")
  print("#####     5 - Módulo Relatório         #####")
  print("#####     6 - Módulo Informações       #####")
  print("#####     0 - Sair                     #####")
  op_princ = input("##### Escolha sua opção: ")

  return op_princ

def menu_cadastrar():
  os.system('clear')
  print()
  print("################################################")
  print("#####   Você está no Módulo Cadastrar   ####")
  print("############################################")
  print("##### 1 - Cadastrar Cachorro           #####")
  print("##### 2 - Cadastrar Serviço            #####")
  print("##### 3 - Cadastrar Agendamento        #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_cad = input("##### Escolha sua opção: ")
  print()
  input("Tecle <ENTER> para continuar...")
  return op_cad

def menu_pesq():
  os.system('clear')
  print()
  print("#############################################")
  print("#####   Você está no Módulo Pesquisar   ####")
  print("############################################")
  print("##### 1 - Pesquisar Cachorro           #####")
  print("##### 2 - Perquisar Serviço            #####")
  print("##### 3 - Pesquisar Agendamento        #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_pesq = input("##### Escolha sua opção: ")
  print()
  input("Tecle <ENTER> para continuar...")

  return op_pesq

def menu_att():
  os.system('clear')
  print()
  print("#############################################")
  print("#####   Você está no Módulo Atualizar   ####")
  print("############################################")
  print("##### 1 - Atualizar Cachorro           #####")
  print("##### 2 - Atualizar Serviço            #####")
  print("##### 3 - Atualizar Agendamento        #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_att = input("##### Escolha sua opção: ")
  print()
  input("Tecle <ENTER> para continuar...")
  
  return op_att
  
def menu_del():
  os.system('clear')
  print()
  print("#############################################")
  print("#####   Você está no Módulo Deletar   ####")
  print("############################################")
  print("##### 1 - Deletar Cachorro             #####")
  print("##### 2 - Deletar Serviço              #####")
  print("##### 3 - Deletar Agendamento          #####")
  print("##### 0 - Retornar ao Menu Principal    #####")
  op_del = input("##### Escolha sua opção: ")
  print()
  input("Tecle <ENTER> para continuar...")

  return op_del

## CADASTRAR
def cad_cachorro():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Cadastra Cachorro        #####")
  print("############################################")
  print()
  nome = input("##### Nome: ")
  print()
  dtnas = input("##### Data de nascimento: ")
  print()
  raca = input("##### Raça: ")
  print()
  fone = input("##### Telefone: ")
  print()
  id = cachorros.__len__() + 1
  id = str(id)
  cachorros[id] = [nome, dtnas, raca, fone]
  print("Cachorro cadastrado com sucesso!")
  print()
  print(cachorros)
  escreverArquivos()
  input("Tecle <ENTER> para continuar...")
  
def cad_servico():
  os.system('clear')
  print()
  print("############################################")
  print("#####       Cadastrar Serviço          #####")
  print("############################################")
  print()
  nome = input("Nome do serviço: ")
  print()
  valor = input("Valor: ")
  id = servicos.__len__() + 1
  id = str(id)
  servicos[id] = [nome, valor]
  print("Serviço cadastrado com sucesso!")
  print()
  #print(servicos)
  escreverArquivos()
  input("Tecle <ENTER> para continuar...")
  
def cad_agenda():
  os.system('clear')
  print()
  print("############################################")
  print("#####        Cadastrar Agendamento     #####")
  print("############################################")
  print()
  id_cachorro = input("###### Cachorro para agendamento: ")
  print()
  id_servico = input("##### Serviço: ")
  print()
  data = input("##### Data e Hora: ")
  id = agenda.__len__() + 1
  id = str(id)
  agenda[id]= [id_cachorro, id_servico, data]
  print("Agendamento feito com sucesso!")
  #print(agenda)
  escreverArquivos()
  input("Tecle <ENTER> para continuar...")


## PESQUISAR

def pes_cachorro():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Pesquisar Cachorro       #####")
  print("############################################")
  print()
  id_cachorro = input("Qual o ID do cachorro que deseja pesquisar? ")
  
  if id_cachorro in cachorros.keys():
    print()
    print("Nome: ", cachorros[id_cachorro][0])
    print("Data de nascimento: ", cachorros[id_cachorro][1])
    print("Raça: ", cachorros[id_cachorro][2])
    print("Telefone: ", cachorros[id_cachorro][3])
  else:
    print("Cachorro não existente! ")

  input("Tecle <ENTER> para continuar...")

def pes_servico():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Pesquisar Serviço        #####")
  print("############################################")
  print()
  id_servico = input("Qual o ID do serviço que deseja pesquisar? ")

  if id_servico in servicos.keys():
    print()
    print("Nome: ", servicos[id_servico][0])
    print("Valor: ", servicos[id_servico][1])
  else:
    print("Serviço não existente! ")

  input("Tecle <ENTER> para continuar...")

def pes_agenda():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Pesquisar Agendamento    #####")
  print("############################################")
  print()
  id_agenda = input("Qual o ID do agendamento que deseja pesquisar? ")

  if id_agenda in agenda.keys():
    print()
    print("Cachorro: ", agenda[id_agenda][0])
    print("Serviço: ", agenda[id_agenda][1])
    print("Data e hora: ", agenda[id_agenda][2])
  else:
    print("Agendamento não existente! ")

  input("Tecle <ENTER> para continuar...")

# ATUALIZAR

def att_cachorro():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Atualizar Cachorro       #####")
  print("############################################")
  print()
  id_cachorro = input("Qual o ID do cachorro? ")
  
  if id_cachorro in cachorros.keys():
    print()
    print("Informe os novos dados: ")
    nome = input("##### Nome: ")
    print()
    dtnas= input("##### Data de Nascimento: ")
    print()
    raca = input("##### Raça: ")
    print()
    fone = input("##### Telefone: ")
    print()
    cachorros[id_cachorro] = [nome, dtnas, raca, fone]
    print("Cachorro alterado com sucesso!")
    #print(cachorros)
    escreverArquivos()
  else:
    print("Cachorro inexistente! ")

  input("Tecle <ENTER> para continuar...")
    
def att_servico():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Atualizar Serviço        #####")
  print("############################################")
  print()
  id_servico = input("Qual o ID do Serviço? ")

  if id_servico in servicos.keys():
    print()
    print("Informes os novos dados: ")
    nome = input("##### Nome: ")
    print()
    valor = input("##### Valor: ")
    print()
    servicos[id_servico] = [nome, valor]
    print("Serviço alterado com sucesso!")
    #print(servicos)
    escreverArquivos()
  else:
    print("Serviço inexistente! ")

  input("Tecle <ENTER> para continuar...")

def att_agenda():
  os.system('clear')
  print()
  print("############################################")
  print("#####       Atualizar Agendamento      #####")
  print("############################################")
  print()
  id_agenda = input("Qual o ID do agendamento? ")

  if id_agenda in agenda.keys():
    print()
    print("Informe os novos dados: ")
    cachorro = input("##### ID do cachorro: ")
    print()
    serv = input("##### ID do serviço: ")
    print()
    data = input("##### Data e Hora: ")
    print()
    agenda[id_agenda] = [cachorro, serv, data]
    print("Agendamento alterado com sucesso!")
    #print(agenda)
    escreverArquivos()
  else:
    print("Agendamento inexistente! ")

  input("Tecle <ENTER> para continuar...")

## DELETAR

def del_cachorro():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Deletar Cachorro         #####")
  print("############################################")
  print()
  id_cachorro = input("Qual o ID do cachorro? ")
  
  if id_cachorro in cachorros.keys():
    resp = input("Tem certeza que deseja deletar o cachorro?(S/N) ")
    if resp == 's' or resp == 'S':
      del cachorros[id_cachorro]
      print("Cachorro deletado com sucesso! ")
      #print(cachorros)
      escreverArquivos()
    else:
      print("Exclusão não realizada! ")
  else:
    print("Cachorro inexistente! ")

  input("Tecle <ENTER> para continuar...")

def del_servico():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Deletar Serviço          #####")
  print("############################################")
  print()
  id_servico = input("Qual o ID do serviço? ")

  if id_servico in servicos.keys():
    resp = input("Tem certeza que deseja deletar o serviço?(S/N) ")
    if resp == 's' or resp == 'S':
      del servicos[id_servico]
      print("Serviço deletado com sucesso! ")
      #print(servicos)
      escreverArquivos()
    else:
      print("Exclusão não realizada! ")
  else:
    print("Serviço inexistente!")

  input("Tecle <ENTER> para continuar...")
  
def del_agenda():
  os.system('clear')
  print()
  print("############################################")
  print("#####       Deletar Agendamento        #####")
  print("############################################")
  print()
  id_agenda = input("Qual o ID o agendamento? ")

  if id_agenda in agenda.keys():
    resp = input("Tem certeza que deseja deletar o cachorro?(S/N) ")
    if resp == 's' or resp == 'S':
      del agenda[id_agenda]
      print("Agendamento deletado com sucesso! ")
      #print(agenda)
      escreverArquivos()
    else:
      print("Exclusão não realizada! ")
  else:
    print("Agendamento inexistente!")

  input("Tecle <ENTER> para continuar...")

def escreverArquivos():
  arq_cachorros = open("cachorros.dat", "wb")
  pickle.dump(cachorros, arq_cachorros)
  arq_cachorros.close()

  arq_servicos = open("servicos.dat", "wb")
  pickle.dump(servicos, arq_servicos)
  arq_servicos.close()

  arq_agenda = open("agenda.dat", "wb")
  pickle.dump(agenda, arq_agenda)
  arq_agenda.close()