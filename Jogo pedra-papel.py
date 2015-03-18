import random
j1 = 0
com = 0
while com<3 and j1<3:
    computador = ['pedra','papel','tesoura','lagarto','spock']
    sorteio = random.choice(computador)
    jogador1 = input('voce quer pedra, papel, tesoura, lagarto ou spock?')
    jogador1 = jogador1.lower()
    if sorteio == jogador1:
        print(' voce jogou %s e o computador jogou %s, EMPATOU'%(jogador1,sorteio))
        print('%s x %s'%(com,j1))
    elif (sorteio == 'pedra' and jogador1=='papel'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'pedra' and jogador1=='tesoura'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'pedra' and jogador1=='lagarto'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'pedra' and jogador1=='spock'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'papel' and jogador1=='pedra'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'papel' and jogador1=='tesoura'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'papel' and jogador1=='lagarto'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'papel' and jogador1=='spock'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'tesoura' and jogador1=='pedra'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'tesoura' and jogador1=='papel'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'tesoura' and jogador1=='lagarto'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'tesoura' and jogador1=='spock'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'lagarto' and jogador1=='pedra'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'lagarto' and jogador1=='papel'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'lagarto' and jogador1=='tesoura'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'lagarto' and jogador1=='spock'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'spock' and jogador1=='pedra'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'spock' and jogador1=='papel'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'spock' and jogador1=='tesoura'):
        print('voce jogou %s e o computador jogou %s, VOCÊ PERDEU'%(jogador1,sorteio))
        com = com+1
        j1 = 0
        print('%s x %s'%(com,j1))
    elif (sorteio == 'spock' and jogador1=='lagarto'):
        print('voce jogou %s e o computador jogou %s, VOCÊ GANHOU'%(jogador1,sorteio))
        j1 = j1+1
        com = 0
        print('%s x %s'%(com,j1))                 
if j1==3:
    print('VOCÊ GANHOU O JOGO, PARABEEEEEEENS')
if com == 3:
    print('VOCÊ PERDEU O JOGO, TENTE NOVAMENTE')