import random #Importa a biblioteca Randon que trabalha com números aleatórios

#palavras = ['abacate','chocolate','paralelepipedo','goiaba']
palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def palavrasescolhidas():#Define a função
    global palavras #Determina que esta variável pertence a todo o programa
    while True: #É a estrutura de repetição que é executada enquanto a condição da instrução for verdadeira
        palavrasescolhidas = input('Digite aqui a palavra que você quer para o jogo:')#input espera que o usuário digite um texto e aperte enter
        if palavrasescolhidas == "": #Bloco de instrução que é executado quando a condição é verdadeira
            break #Faz com que a execução do progama saia do loop while
    palavras.append(palavrasescolhidas)

def principal():#Define uma função
    """
    Função Princial do programa
    """
    print('F O R C A')#Determina o que será impresso na tela
    palavrasescolhidas() #Chama a função
    palavraSecreta = sortearPalavra()#A variável (palavraSecreta) chama uma função(sortearPalavra())
    palpite = ''#Pede o palpite de uma letra sobre a palavra sorteada
    desenhaJogo(palavraSecreta,palpite)

    while True:#É a estrutura de repetição que é executada enquanto a condição da instrução for verdadeira
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():#Bloco de instrução que é executado quando a condição é verdadeira
            print('Voce Perdeu!!!')
            break #Faz com que a execução do progama saia do loop while
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG #Determina que esta variável pertence a todo o programa
    if len(letrasErradas) == len(FORCAIMG):#len é uma função que retorna um valor do tipo inteiro representando a quantidade de caracteres contidos na string
        return True #Faz com que a função retorne se a condição do bloco if for verdadeiro
    else: #É executado quando a condição if acima for falsa
        return False  #Faz com que a função retorne se a condição do bloco if for falso
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True #Torna a variável verdadeira
    for letra in palavraSecreta: #For gera um loop dentro de uma lista e in indica a lista que será utilizada
        if letra not in letrasCertas:#not in diz que não está em
            ganhou = False #False torna a variável é falsa
    return ganhou #Return retorna o valor da variável         
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")#input espera que o usuário digite um texto e aperte enter
    palpite = palpite.upper() #Torna todos os caracteres maiúsculos
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:#elif atribui uma condição a else. É executado quando todas as outras condições são falsas, in quer dizer EM se algo está em, or quer dizer OU isso ou isso
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":#Nega a função do elif
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):#range gera uma lista
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper() #Elemento aleatório a partir de uma sequencia

    
principal()
