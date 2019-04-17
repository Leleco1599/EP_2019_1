# EP 2019-1: Escape Insper
#
# Alunos: 
# aluno A - Alexandre Markiewicz Fernandes, alexandremf6@al.insper.edu.br
# aluno B - Luiz Felipe Valente, luizfdv@al.insper.edu.br

#--------- AREA DE IMPORTS -----------
import random

#--------- EVENTO RANDOM ------------
def evento():
    x = random.randint(1,2)
    return x


#--------- FUNCAO CENARIOS -----------
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "405": "Ir para a sala 405",
                "inventario": "Abrir o seu inventario",
            },
            "evento":False,
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
            },
            "evento": True,
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {},
            "evento": False,
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            },
            "evento": True,
        },
        "405": {
            "titulo": "Sala 405",
            "descricao":"Cheiro de Doritos?! Você está na sala 405",
            "opcoes": {
                "falar com veteras": "Falar com um veterano: 'Me salva mein'",
                "pegar canetao": "Roubar um canetão...",
                "404": "Ir para sala 404",
                "406": "Ir para a 406....... cuidado...",
                "inicio": "Tomar o elevandor para o saguao de entrada",
                },
            "evento": True,
        },
        "404": {
            "titulo": "Sala 404",
            "descricao": "Error 404: Page Not Found",
            "opcoes": {
                "falar com tecnico": "Falar com tecnico: 'Marcão me salva!'",
                "brincar com robo": "Voce achou um robo muito daora parça",
                "405": "Voltar para sala 405",
                },
            "evento": True,
        },
        "406": {
            "titulo": "Bem vindo a sala 406",
            "descricao": "Aquela nostalgia de estudar desesperado pras PF's com o ar no 16°... AH! e nesta sala você pode se TELETRANSPORTAR para qualquer outra sala desde que lembre o nome! Aproveite :)",
            "opcoes": {
                    "405": "Voltar para sala 405",
#                    "tp random": "Teleporte para cenario aleatorio... Este é para aventureiros eihn?... hehehe",
                    "tp escolha": "Teletransporte para onde quiser!",
                    },
            "evento": True,
        },
    }
    nome_cenario_atual = "inicio"
    return (cenarios, nome_cenario_atual)

#--------- FUNCAO INVENTARIO -----------
def funcao_inventario():
    invent = {"RedBull": 0,
                  "Partes EP": 0,}
    return invent

#-------- PROGRAMA QUE RODA O JOGO ----------

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    
#------ DECLARANDO VARIAVEIS ---------
    cenarios, nome_cenario_atual = carregar_cenarios()
    invent = funcao_inventario()
    lista_cenarios = []
    for k in cenarios.keys():
        lista_cenarios.append(k)
    vida_personagem = 100
    game_over = False
    cenario_atual = cenarios[nome_cenario_atual]
#------------------------------------
    
    while not game_over:
        
        if cenario_atual["evento"] == True:
                numero = evento()
                
                if numero == 1:
                    print ("*** Você ganhou uma RedBull! ***")
                    print()
                    print("Você pode bebe-lo ou guardalo no seu inventário!")
                    opcoes_redbull = input("beber ou guardar?: ")
                    if opcoes_redbull == "beber":
                        vida_personagem += 20
                        print("agora você tem {0} de vida!".format(vida_personagem))
                        
                    elif opcoes_redbull == "guardar":
                        invent["RedBull"] += 1
                        print("Seu Redbull foi adicionado! Agora você tem {0}".format(invent))
                
                if numero == 2:
                    print("*** Um monstro apareceu! Ele fez você perder tempo! ***")
                    vida_personagem -= 30
                    print("Agora você tem {0} de vida!".format(vida_personagem))
                    print()
                    print("#####################")
                    print()
                    if vida_personagem <= 0:
                        break
                
        
        comprimento_do_cenario = len(nome_cenario_atual)
        print(nome_cenario_atual)
        print(comprimento_do_cenario * "-")
        print(cenario_atual["descricao"])
        

        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
            
        else:
            
            print('Escolha sua opção: ')
            
            for k,v in opcoes.items():
                print(k,':',v)
                
            escolha = input("O que você quer fazer: ")
            print()
            print()
            print("#####################")
            print()


#              ------- TELEPORTE -------
            
            if nome_cenario_atual == "406" and escolha == "tp escolha":
                destino = input("Para onde você quer ir?: ")
                if destino in lista_cenarios:
                    nome_cenario_atual = destino
#              ------ FIM DO TELEPORTE ------
                    
            elif nome_cenario_atual == "inicio" and escolha == "inventario":
                tomar_rb = input("Você quer tomar um RedBull? (s/n): ")
                if tomar_rb == "s" and invent["RedBull"] != 0:
                    invent["RedBull"] -= 1
                    vida_personagem += 20
                    print("agora você tem {0} de vida!".format(vida_personagem))
                    
                elif tomar_rb == "n":
                    nome_cenario_atual = "inicio"        
            
            
            elif escolha in opcoes and escolha != "tp escolha" and escolha != "inventario":
                nome_cenario_atual = escolha
                
                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                
            cenario_atual = cenarios[nome_cenario_atual]

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()