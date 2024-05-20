from funcoes import (menu_att, menu_del, menu_principal, menu_cadastrar, menu_pesq,
                     cad_cachorro, cad_agenda, cad_servico, menu_principal,
                     pes_agenda, pes_cachorro, pes_servico, att_cachorro,
                     att_agenda, att_servico, del_cachorro, del_servico,
                     del_agenda, escreverArquivos)

#####################################
##### Projeto Pet Shop - PRINCIPAL #####
#####################################
## falta terminar pesquisas
op_princ = ''
while op_princ != '0':
  op_princ = menu_principal()
  if op_princ == '1':
    op_cad = ''
    while op_cad != '0':
      op_cad = menu_cadastrar()
      if op_cad == '1':
        cad_cachorro()
      elif op_cad == '2':
        cad_servico()
      elif op_cad == '3':
        cad_agenda()
        
  elif op_princ == '2':
    op_pesq = ''
    while op_pesq != '0':
      op_pesq = menu_pesq()
      if op_pesq == '1':
        pes_cachorro()
      elif op_pesq == '2':
        pes_servico()
      elif op_pesq == '3':
        pes_agenda()

  elif op_princ == '3':
    op_att = ''
    while op_att != '0':
      op_att = menu_att()
      if op_att == '1':
        att_cachorro()
      elif op_att == '2':
        att_servico()
      elif op_att == '3':
        att_agenda()

  elif op_princ == '4':
    op_del = ''
    while op_del != '0':
      op_del = menu_del()
      if op_del == '1':
        del_cachorro()
      elif op_del == '2':
        del_servico()
      elif op_del == '3':
        del_agenda()

  elif op_princ == '5':
    print()
    print("############################################")
    print("#####  Você está no Módulo Relatório    ####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar...")
  elif op_princ == '6':
    print()
    print("############################################")
    print("#####  Você está no Módulo Informações  ####")
    print("############################################")
    print()
    print("##### Projeto de Gestão de um Pet Shop  ####")
    print("##### Equipe de desenvolvimento:        ####")
    print("##### Ariadny Dantas @ariadnydantas71   ####")
    print("##### Licença Pública Geral GNU         ####")
    print("##### www.gnu.org/licenses/gpl.html     ####")
    print()
    input("Tecle <ENTER> para continuar...")

print("Você encerrou o programa!")
print("Até logo!")

escreverArquivos()