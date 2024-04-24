nome = input("Insira seu nome: ")
def Chatbot(N): #Inicio do programa
    print(f"Ola {N}, aqui é o ChatBot de Assistência da IATech,Em que posso ser Util?")
    print("Por Favor,Insira o Número Correspondente ao seu Problema")

    #Respostas
    O1 = "Acionar a Garantia de Algum produto" 
    O2 = "Problemas com PC"
    O3 = "Problmas com Pagamento"
    O4 = "Outro Problema"

    #Printando Opções Na Tela
    print(f"1 - {O1}\n"
        f"2 - {O2}\n"
        f"3 - {O3}\n"
        f"4 - {O4}\n")

    #Opções Robotizadas do programa para seleção
    def Opcoes(R): 
        #SESSAO AUTOMATIZADA
        selecao = "Você Selecionou a Opção"
        num = "Insira o Número Correspondente ao seu Problema"
        manuntencao = (f"Desculpe essa Linha do Serviço esta com Sobrecarga ou em Manuntenção, Porfavor Tente novamente mais tarde")

        #Sessão de Seleção

        #Conversa 1
        if R == 1:
            print(selecao,f"'{O1}',Correto?")
            R2 = input("Confirme (S/N):")
            if R2 == "S" or "Sim":
                print("")
            else:
                print(f"Porfavor,Tente dnv\n {num}")
                resposta = input("")
                Opcoes(resposta)
                
      #Conversa 2
        elif R == 2:
            print(selecao,f"'{O2}',Correto?")
            R2 = input("Confirme (S/N):")
            if R2 == "S" or "Sim":
                print(manuntencao)
            else:
                print(f"Porfavor,Tente dnv\n {num}")
                resposta = input()
                Opcoes(resposta)
        
        #Conversa 3
        elif R == 3:
            print(selecao,f"'{O3}',Correto?")
            R2 = input("Confirme (S/N):")
            if R2 == "S" or "Sim":
                print(manuntencao)
            else:
                print(f"Porfavor,Tente dnv\n {num}")
                resposta = input()
                Opcoes(resposta)
        
        #Conversa 4
        elif R == 4:
            print(selecao,f"'{O4}',Correto?")
            R2 = input("Confirme (S/N):")
            if R2 == "S" or "Sim":
                print(manuntencao)
            else:
                print(f"Porfavor,Tente dnv\n {num}")
                resposta = input()
                Opcoes(resposta)
        else:
            print(f"Sinto Muito {N}, Não Compreendi Porfavor Tente De novo")
            resposta = input()
            Opcoes(resposta)
        

    resposta = int(input("Insir Número: ")) #Entrada da Resposta Inicial do Usuário
    Opcoes(resposta)
Chatbot(nome)