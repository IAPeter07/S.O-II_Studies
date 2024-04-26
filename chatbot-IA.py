nome = input("Para começar Insira seu nome: ")
def Chatbot(N): #Inicio do programa
    print(f"Ola {N}, aqui é o ChatBot de Assistência da 'IATech',Em que posso ser Util?\n")
    print("Por Favor,Insira o Número Correspondente ao seu Problema:")

    #Respostas
    O1 = "Acionar a Garantia de Algum produto" 
    O2 = "Rastrear Produto"
    O3 = "Problemas com Pagamento"
    O4 = "Outro(s)"

    #Printando Opções Na Tela
    print(f"1 - {O1}\n"
        f"2 - {O2}\n"
        f"3 - {O3}\n"
        f"4 - {O4}\n")

    resposta = int(input("Escolher Número: ")) #Entrada da Resposta Inicial do Usuário
    #Opções Robotizadas do programa para seleção
    def Opcoes(R): 
        #variaveis de resposta
        manuntencao = (f"Desculpe essa Linha do Serviço esta com Sobrecarga ou em Manuntenção, Porfavor Tente novamente mais tarde")
        tryagain = ("Alguma Coisa está errada,Porfavor Tente dnv")
        #Sessão de Seleção

        #Conversa 1
        if (R == 1):
            print(f"Você Selecionou a Opção,'{O1}',Correto?")
            R2 = input("Confirme (S/N): ")
            if (R2 == "Sim") or (R2 =="S") or (R2 =="s"):
                print("Certo, Informe o Produto e Código de Serie Para Continuar o Procedimento")
                R3_Prod = str(input("Nome do Produto: "))
                R3_Cod = str(input("Código de Serie: "))
                if (R3_Prod and R3_Cod != ""): #Se as respostas não forem'vazio'
                    print(f"O Produto Informado é: {R3_Prod}, e O Código do Produto: {R3_Cod}, Certo?")
                    R4=input("Confirme (S/N): ")
                    if (R4 == "Sim") or (R4 =="S") or (R4 =="s"):
                        print("Certo, Agora gostariamos que descrevesse brevemento o problema ocorrido para nossa equipe avaliar a situação.")
                        R5 = input("Insira o problema: ")
                        if (R5 != ""):
                            print(f"Certo {N}, Nossa equipe analisara o seu caso conforme as Informações passadas, Informe seu email para retorno")
                            r_email = input("Infome seu Email: ")
                            if not isinstance(r_email,int) or (r_email is not None):
                                print("Tudo pronto agradecemos a paciência, retornaremos o contato")
                            else:
                                print("Email Invalido,Tente Novamente")
                                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                                resposta = int(input("Escolher Número: "))
                                Opcoes(resposta)
                        else:
                            print(tryagain)
                            print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                            resposta = int(input("Escolher Número: "))
                            Opcoes(resposta)
                    else:
                        print(tryagain)
                        print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                        resposta = int(input("Escolher Número: "))
                        Opcoes(resposta)
                else: 
                    print(tryagain)
                    print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                    resposta = int(input("Escolher Número: "))
                    Opcoes(resposta)
            else:
                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                resposta = int(input("Escolher Número: "))
                Opcoes(resposta)
                
      #Conversa 2
        elif (R == 2):
            print(f"Você Selecionou a Opção,'{O2}',Correto?")
            R2 = input("Confirme (S/N): ")
            if(R2 == "Sim") or (R2 =="S") or (R2 =="s"):
                print("Certo, Informe seu CPF e Código de Rastreio")
                R3_cpf = int(input("Informe CPF: "))
                R3_codR = str(input("Informe Código de Rastreamento: "))
                if  (R3_cpf == ""):
                    print("CPF Invalido,Porfavor Tente dnv")
                    print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                    resposta = int(input("Escolher Número: "))
                    Opcoes(resposta)
                if (R3_codR == ""):
                    print(tryagain)
                    print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                    resposta = int(input("Escolher Número: "))
                    Opcoes(resposta)
                else:
                    print(f"Seu CPF é: {R3_Prod}, e O Código de Rastreio: {R3_codR}, Certo?")
                    R4=input("Confirme (S/N):")
                    if (R2 == "Sim") or (R2 =="S") or (R2 =="s"):
                        print(f"Certo Seu pedido {R3_codR}, Saio da Afilial da IATech\n"
                              "Trafégo - Curitiba")
                    else:
                        print("Porfavor Tente De novo")
                        print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                    resposta = int(input("Escolher Número: "))
                    Opcoes(resposta)
            else:
                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                resposta = int(input("Escolher Número: "))
                Opcoes(resposta)
        
        #Conversa 3
        elif R == 3:
            print(f"Você Selecionou a Opção,'{O3}',Correto?")
            R2 = input("Confirme (S/N): ")
            if(R2 == "Sim") or (R2 =="S") or (R2 =="s"):
                print(manuntencao)
                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                resposta = int(input("Escolher Número: "))
                Opcoes(resposta)
            else:
                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                resposta = int(input("Escolher Número: "))
                Opcoes(resposta)
        
        #Conversa 4
        elif R == 4:
            print(f"Você Selecionou a Opção,'{O4}',Correto?")
            R2 = input("Confirme (S/N): ")
            if(R2 == "Sim") or (R2 =="S") or (R2 =="s"):
                print(manuntencao)
                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                resposta = int(input("Escolher Número: "))
                Opcoes(resposta)
            else:
                print(f"1 - {O1}\n2 - {O2}\n3 - {O3}\n4 - {O4}\n")
                resposta = int(input("Escolher Número: "))
                Opcoes(resposta)
        else:
            print(f"Sinto Muito {N} Não Compreendi, Porfavor Tente De novo")
            resposta = int(input("Escolher Número: "))
            Opcoes(resposta)
    Opcoes(resposta)
Chatbot(nome)