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
            },
            "evento": "False",
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
            },
            "evento": "True",
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {},
            "evento": "False",
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            },
            "evento": "True",
        }
    }
    nome_cenario_atual = "inicio"
    return (cenarios, nome_cenario_atual)


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

    cenarios, nome_cenario_atual = carregar_cenarios()
    vida_personagem = 100
    game_over = False
    cenario_atual = cenarios[nome_cenario_atual]
    while not game_over:
        
        if cenario_atual["evento"] == "True":
                numero = evento()
                
                if numero == 1:
                    print ("Você ganhou uma RedBull!")
                    vida_personagem += 20
                    print(vida_personagem)
                
                if numero == 2:
                    print("Um monstro apareceu! Ele fez você perder tempo!")
                    vida_personagem -= 30
                    print("agora você tem {0} de vida!".format(vida_personagem))
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
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                
            cenario_atual = cenarios[nome_cenario_atual]

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
