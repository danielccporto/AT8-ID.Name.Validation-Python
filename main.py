nomes = []
sobrenomes = []
datas = []
cpfs = []
IDs = []
indice1=0
indice2=0
listaopcoes = [1,2,3,4,5,6]

nome = ""
nome1= ""
nome2= ""
sobrenome = ""
data = ""
CP = 0
cadastro = 0
cadastro_2 = 0


print("1.Inserir novo cadastro:")
print("2.Alterar CPF: ")
print("3.Trocar Sobrenomes: ")
print("4.Remover cadastro: ")
print("5. Listar todos os cadastros.")
print("6. Encerrar")


opcao = int(input("Insira o número da sua escolha: "))

while opcao in listaopcoes :

  if opcao == 1:
    
    cadastro = (input("Digite seu ID: "))
    
    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")
      
    else:
      if cadastro in IDs:
        print(f"O ID {cadastro} já está cadastrado.")
        
      nome = input("Digite seu nome: ")
      nome = nome.capitalize()
      
      if " " in nome: 
        print("O nome não pode ter espaço.")
        
      else:
        sobrenome = input("Digite seu sobrenome: ")
        sobrenome.capitalize()
        
        if " " in sobrenome: 
          print("O sobrenome não pode ter espaço")
          
        else:
          data = input("Digite sua data de nascimento: ")
          CP = input("Digite seu CPF: ")
          print("Seu nome e sobrenome foi formatado e registrado com sucesso.")
          
          if cadastro in IDs: 
            IDs.insert(int(cadastro) -1, cadastro)
            nomes.insert(int(cadastro) -1, nome)
            sobrenomes.insert(int(cadastro) -1, sobrenome)
            cpfs.insert(int(cadastro) -1, CP)
            datas.insert(int(cadastro) -1, data)
            print("O novo cadastro foi registrado. ")
            print(f"Cadastro : {cadastro}, IDs : {IDs[int(cadastro)]}")
            
          else: 
            nomes.append(nome)
            sobrenomes.append(sobrenome)
            IDs.append(cadastro)
            datas.append(data)
            cpfs.append(CP)
            print("Cadastro realizado com sucesso!")
      

  elif opcao == 2 : 
    cadastro = (input("Digite seu ID: "))

    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")
      
    else:
      if cadastro in IDs:
        print(f"O ID {cadastro} já está cadastrado.")
        
        CP = input("Digite o novo CPF: ")
        cpfs[int(cadastro) -1] = CP
        
        print(f"O CPF {cpfs[int(cadastro)-1]} foi alterado com sucesso!")
      
      else: 
        print("O CPF não consta no sistema, tente de novo.")
 
  elif opcao == 3:
    cadastro = (input("Digite seu ID: "))

    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")

    else:
      if cadastro in IDs:
        
        print(f"O ID {cadastro} já está cadastrado.")
        cadastro_2 = input("Digite o 2o ID de registro a ser alterado: ")
        
        nome1 = sobrenomes[int(cadastro) -1]
        nome2 = sobrenomes[int(cadastro_2) -1]
        
        print(f"nome1: {nome1}, nome2 : {nome2}")
        
        sobrenomes[int(cadastro) -1] = nome2
        sobrenomes[int(cadastro_2) -1] = nome1
        
        print(f"sobrenome1: {sobrenomes[int(cadastro) -1]} e sobrenome 2 : {sobrenomes[int(cadastro_2) -1]}")


      else:
        print(f"O sobrenome não existe!")

  elif opcao == 4  :
    cadastro = (input("Digite seu ID: "))

    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")

    else:
      if cadastro in IDs:

        print(f"O ID {cadastro} já está cadastrado.")
        
        del nomes[int(cadastro)-1]
        del sobrenomes[int(cadastro)-1]
        del datas[int(cadastro)-1]
        del cpfs[int(cadastro)-1]
        del IDs[int(cadastro)-1]
        print(f"O ID {cadastro} foi removido!")

      else: 
       print(f"O ID {cadastro} não existe.")

  elif opcao == 5:
    for i in range(len(IDs)):
      print(f"Nome : {nomes[int(i)]}, CPF : {cpfs[int(i)]}, Data de nascimento : {datas[int(i)]}, ID : {IDs[int(i)]}")

  elif opcao == 6:
    print("O programa está sendo encerrado.")
    break
    
    

  print("1.Inserir novo cadastro:")
  print("2.Alterar CPF: ")
  print("3.Trocar Sobrenomes: ")
  print("4.Remover cadastro: ")
  print("5. Listar todos os cadastros.")
  print("6. Encerrar")
  opcao = int(input("Escolha uma opção: "))