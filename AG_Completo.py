from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt
import csv

# Parametros para o funcionamento do algoritmo Genético
tamanhopop = 100  # Número de Individuos
tamanhoindividuo = 50  # Tamanho de bits de cada indivíduo
taxadecruzamento = 75
taxamutacao = 1
geracao = 100
elitismo = False
normalizacao= False
tipo_cruzamento = 3 #1 Cruzamento de 1 ponto de corte ; 2 - Com 2 pontos de corte ; 3 - Uniforme

def criarpop(tamanhopop, tamanhoindiviuo):
    pop = []
    aux = []
    for i in range(0, tamanhopop):
        for j in range(0, tamanhoindiviuo):
            aux.append(randint(0, 1))
        pop.append(aux)
        aux = []
    return pop

def decodint(vetor_populacao):
    inteirox_y = []
    for k in range(0, tamanhopop):
        somax = 0
        somay = 0
        aux = []
        individuo_binario = vetor_populacao[k]
        for i in range(0, 25):
            if individuo_binario[i]:
                somax += 1 * 2 ** i
        for j in range(25, 50):
            if individuo_binario[j]:
                somay += 1 * 2 ** (j - 26)
        aux.append(somax)
        aux.append(somay)
        inteirox_y.append(aux)
    return inteirox_y

def decodreal(inteirox_y):
    realx_y = []
    for k in range(0, tamanhopop):
        valorrealx = 0
        valorrealy = 0
        aux = []
        individuo_inteiro = inteirox_y[k]
        valorrealx = ((individuo_inteiro[0] * (200 / 33554431)) - 100)
        valorrealy = ((individuo_inteiro[1] * (200 / 33554431)) - 100)
        aux.append(valorrealx)
        aux.append(valorrealy)
        realx_y.append(aux)

    return realx_y

def fitness(vetor_real):
    pop_avaliada = []
    for k in range(0, tamanhopop):
        valor_z = 0
        individuo_real = vetor_real[k]
        x = individuo_real[0]
        y = individuo_real[1]
        valor_z = 0.5 - (((np.sin(np.sqrt(x ** 2 + y ** 2)))
         ** 2 - 0.5) / (1 + (0.001 * (x ** 2 + y ** 2)) ** 2))
        pop_avaliada.append(valor_z)
    return pop_avaliada

def rankear(pop_atual, pop_avaliada):
    popmatriz = np.column_stack((pop_atual, pop_avaliada))
    matriz_rankeada = sorted(popmatriz, key=lambda popmatriz: popmatriz[50])
    popatualrankeada = []
    popavaliadarankeada = []
    aux = []
    for i in range(0,len(pop_atual)):
        popavaliadarankeada.append(matriz_rankeada[i][50])
        for j in range(0,tamanhoindividuo):
            if matriz_rankeada[i][j] == 0.0:
                aux.append(0)
            else:
                aux.append(1)
        popatualrankeada.append(aux)
        aux = []
    return popatualrankeada

def normalizacaolinear():
    avaliacao = []
    for i in range(1,tamanhopop+1):
        avaliacao.append(10+((500-10)*(i-1))/(tamanhopop - 1))
    return avaliacao

def selecao(vetor_populacao, vetor_avaliado):
    soma_aptidao = 0

    for i in range(0, len(vetor_avaliado)):
        soma_aptidao += vetor_avaliado[i]
    selecionado = []
    r = 0
    acumulador = 0
    aux = []
    r = uniform(0, soma_aptidao)
    for k in range(0, len(vetor_avaliado)):
        acumulador += vetor_avaliado[k]
        if acumulador >= r:
            selecionado = vetor_populacao[k]
            break

    return selecionado

def cruzamento(vetor_pop, vetor_aptidao, txcruzamento):
    pop_filho = []
    while len(vetor_pop) != len(pop_filho):
        testecruzamento = randint(0, 100)
        if testecruzamento <= txcruzamento:
            filho1 = []
            filho2 = []
            pai1 = selecao(vetor_pop, vetor_aptidao)
            pai2 = selecao(vetor_pop, vetor_aptidao)

            if (tipo_cruzamento == 1): #1 Ponto de corte
                ponto = randint(1, 49)
                for k in range(0, ponto):
                    filho1.append(pai2[k])
                    filho2.append(pai1[k])
                for i in range(ponto, 50):
                    filho1.append(pai1[i])
                    filho2.append(pai2[i])
            elif(tipo_cruzamento == 2): #2 Pontos de corte
                ponto1 = randint(1,47)
                ponto2 = randint(1,47)
                if(ponto2 < ponto1):
                    aux = ponto1
                    ponto1 = ponto2
                    ponto2 = aux
                for i in range(0, ponto1):
                    filho1.append(pai1[i])
                    filho2.append(pai2[i])
                for k in range(ponto1,ponto2):
                    filho1.append(pai2[k])
                    filho2.append(pai1[k])
                for j in range(ponto2, 50):
                    filho1.append(pai1[j])
                    filho2.append(pai2[j])
            else:                       #Uniforme
                padrao = []
                for i in range(0,50):
                    bit = randint(0,1)
                    padrao.append(bit)
                for i in range(0, 50):
                    if(padrao[i] == 0):
                        filho1.append(pai1[i])
                        filho2.append(pai2[i])
                    else:
                        filho1.append(pai2[i])
                        filho2.append(pai1[i])
            pop_filho.append(filho1)
            pop_filho.append(filho2)    
    return pop_filho

def mutacao(populacaoatual, txmutacao):
    pop = populacaoatual
    populacaomutada = []
    for k in range(0, len(pop)):
        individuo = pop[k]
        for i in range(0, len(individuo)):
            testemutacao = randint(0, 100)
            if testemutacao <= txmutacao:
                ponto = randint(0, 50)
                if individuo[i] == '0':
                    individuo[i] = '1'
                if individuo[i] == '1':
                    individuo[i] = '0'
        populacaomutada.append(individuo)
    return populacaomutada

def selecaomaisapto(pop_avaliada, vetor_populacao):
    maisapto = 0
    melhorindividuo = []
    for i in range(0, len(pop_avaliada)):
        if maisapto < pop_avaliada[i]:
            maisapto = pop_avaliada[i]
            melhorindividuo = vetor_populacao[i]
    return maisapto, melhorindividuo

def selecaomenosapto(pop_avaliada):
    menosapto = 1000
    for i in range(0, len(pop_avaliada)):
        if menosapto > pop_avaliada[i]:
            menosapto = pop_avaliada[i]
    return menosapto

def media(ensaio1, ensaio2, ensaio3, ensaio4, ensaio5, ensaio6, ensaio7, ensaio8, ensaio9, ensaio10, ensaio11, ensaio12,
          ensaio13, ensaio14, ensaio15, ensaio16, ensaio17, ensaio18, ensaio19, ensaio20, ensaio21, ensaio22, ensaio23,
          ensaio24, ensaio25, ensaio26, ensaio27, ensaio28, ensaio29, ensaio30):
    media = []
    for i in range(0, len(ensaio1)):
        media.append((ensaio1[i] + ensaio2[i] + ensaio3[i] + ensaio4[i] + ensaio5[i] +
                      ensaio6[i] + ensaio7[i] + ensaio8[i] + ensaio9[i] + ensaio10[i] + ensaio11[i] +
                      ensaio12[i] + ensaio13[i] + ensaio14[i] + ensaio15[i] + ensaio16[i] + ensaio17[i] +
                      ensaio18[i] + ensaio19[i] + ensaio20[i] + ensaio21[i] + ensaio22[i] + ensaio23[i] +
                      ensaio24[i] + ensaio25[i] + ensaio26[i] + ensaio27[i] + ensaio28[i] + ensaio29[i] +
                      ensaio30[i]) / 30)
    return media

def main(geracao, pop_atual, taxadecruzamento, taxamutacao):
    individuomaisapto=[]
    individuomenosapto=[]
    melhorindividuo = 0
    ponto = 0
    indmaisaptogeraçao = 0
    mediapop = []  
    x_y_fitness = []
    melhoresindensaios = []
    for i in range(0, geracao):
        popinteiro=decodint(pop_atual)
        popreal=decodreal(popinteiro)
        popavaliada = fitness(popreal)
        indmaisapto = selecaomaisapto(popavaliada,pop_atual)[0]
        if not normalizacao:  
            individuomaisapto.append(indmaisapto)
            melhorindividuo = selecaomaisapto(popavaliada,pop_atual)[1]
            individuomenosapto.append(selecaomenosapto(popavaliada))
            soma_aptidao = 0
            for i in range(0, len(popavaliada)):
                soma_aptidao += popavaliada[i]
            mediapop.append(soma_aptidao/len(popavaliada))
            pop_filhos = cruzamento(pop_atual, popavaliada, taxadecruzamento)
            pop_filhosmutados = mutacao(pop_filhos, taxamutacao)
            pop_atual = pop_filhosmutados
            
        else:
            poprankeada = rankear(pop_atual, popavaliada)
            melhorindividuo = poprankeada[99]
            popnormalizada = normalizacaolinear()
            pop_filhos = cruzamento(poprankeada, popnormalizada, taxadecruzamento)
            pop_filhosmutados = mutacao(pop_filhos, taxamutacao)
            pop_atual = pop_filhosmutados
            individuomaisapto.append(selecaomaisapto(popavaliada,pop_atual)[0])
            individuomenosapto.append(selecaomenosapto(popavaliada))
            soma_aptidao = 0
            for i in range(0, len(popavaliada)):
                soma_aptidao += popavaliada[i]
            mediapop.append(soma_aptidao/len(popavaliada))
        if elitismo:
            ponto = randint(0, 99)
            pop_atual[ponto] = melhorindividuo
        
        if indmaisaptogeraçao < indmaisapto:
            indmaisaptogeraçao = indmaisapto

    return (pop_atual, individuomaisapto, individuomenosapto,mediapop, x_y_fitness, indmaisaptogeraçao)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]


ensaios = []
# melhor_fitness_por_ensa = []

for i in range(0,10):
    popatual = criarpop(tamanhopop, tamanhoindividuo)
    print(i)
    for k in range(0,3):
        individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[3]
        # melhor_fitness_por_ensa.append(individuomaisapto)
        ensaios.append(individuomaisapto)
# c = csv.writer(open('melhorindporensaio.csv', 'w')) 
# c.writerow(melhor_fitness_por_ensa)
aux0 = ensaios[0]
aux1 = ensaios[1]
aux2 = ensaios[2]
aux3 = ensaios[3]
aux4 = ensaios[4]
aux5 = ensaios[5]
aux6 = ensaios[6]
aux7 = ensaios[7]
aux8 = ensaios[8]
aux9 = ensaios[9]
aux10 = ensaios[10]
aux11 = ensaios[11]
aux12 = ensaios[12]
aux13 = ensaios[13]
aux14 = ensaios[14]
aux15 = ensaios[15]
aux16 = ensaios[16]
aux17 = ensaios[17]
aux18 = ensaios[18]
aux19 = ensaios[19]
aux20 = ensaios[20]
aux21 = ensaios[21]
aux22 = ensaios[22]
aux23 = ensaios[23]
aux24 = ensaios[24]
aux25 = ensaios[25]
aux26 = ensaios[26]
aux27 = ensaios[27]
aux28 = ensaios[28]
aux29 = ensaios[29]

media = media(aux0, aux1, aux2, aux3, aux4, aux5, aux6, aux7, aux8, aux9, aux10, aux11, aux12, aux13, aux14, aux15,
              aux16, aux17, aux18, aux19, aux20, aux21, aux22, aux23, aux24, aux25, aux26, aux27, aux28, aux29)

fig =  plt.figure()
# x = np.linspace(0, 100, 20)
# plt.subplot(3,1,1)
plt.plot(media,'g-')
# plt.grid(True)
# plt.subplot(3,1,2)
# plt.plot(individuomaisapto, 'r-')
# plt.grid(True)
# plt.subplot(3,1,3)
# plt.plot(individuomaisapto, 'r-')
plt.title('Média de toda população do ag canônico com Cruzamento uniforme',fontsize ='medium')
plt.ylabel(u'Individuos')
plt.xlabel(u'Gerações')
plt.grid(True)
plt.show()