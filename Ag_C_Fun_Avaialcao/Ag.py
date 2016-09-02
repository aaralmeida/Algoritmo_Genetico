from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt

# Parametros para o funcionamento do algoritmo Genético
tamanhopop = 100  # Número de Individuos
tamanhoindividuo = 50  # Tamanho de bits de cada indivíduo
taxadecruzamento = 75
taxamutacao = 1
geracao = 100
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
        valor_z = 999.5 - (((np.sin(np.sqrt(x ** 2 + y ** 2)))
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
    return popatualrankeada, popavaliadarankeada

def funcaoavaliacao():
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
    pop = vetor_pop
    while len(pop) != len(pop_filho):
        filho1 = []
        filho2 = []
        pai1 = selecao(vetor_pop, vetor_aptidao)
        pai2 = selecao(vetor_pop, vetor_aptidao)
        testecruzamento = randint(0, 100)
        ponto = randint(1, 49)
        if testecruzamento <= txcruzamento:
            for k in range(0, ponto):
                filho1.append(pai2[k])
                filho2.append(pai1[k])
            for i in range(ponto, 50):
                filho1.append(pai1[i])
                filho2.append(pai2[i])
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

def selecaomaisapto(pop_avaliada,pop_atual):
    maisapto = 0
    for i in range(0, len(pop_avaliada)):
        if maisapto < pop_avaliada[i]:
            maisapto = pop_avaliada[i]
            individuo = pop_atual[i]
    return maisapto

def selecaomenosapto(pop_avaliada):
    menosapto = 1
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
                      ensaio4[i] + ensaio7[i] + ensaio8[i] + ensaio9[i] + ensaio10[i] + ensaio11[i] +
                      ensaio12[i] + ensaio13[i] + ensaio14[i] + ensaio15[i] + ensaio16[i] + ensaio17[i] +
                      ensaio18[i] + ensaio19[i] + ensaio20[i] + ensaio21[i] + ensaio22[i] + ensaio23[i] +
                      ensaio24[i] + ensaio25[i] + ensaio26[i] + ensaio27[i] + ensaio28[i] + ensaio29[i] +
                      ensaio30[i]) / 30)
    return media

def main(geracao, pop_atual, taxadecruzamento, taxamutacao):
    individuomaisapto=[]
    individuomenosapto=[]
    for i in range(0, geracao):
        popinteiro=decodint(pop_atual)
        popreal=decodreal(popinteiro)
        popfitness = fitness(popreal)
        poprankeada = rankear(pop_atual, popfitness)[0]
        melhorindividuo = poprankeada[99]
        popavaliada = funcaoavaliacao()
        pop_filhos = cruzamento(poprankeada, popavaliada, taxadecruzamento)
        pop_filhosmutados = mutacao(pop_filhos, taxamutacao)
        pop_atual = pop_filhosmutados
        pop_atual[5] = melhorindividuo
        individuomaisapto.append(selecaomaisapto(popfitness,pop_atual))
    return (pop_atual, individuomaisapto, individuomenosapto)

popatual = criarpop(tamanhopop, tamanhoindividuo)
individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]


# vetor_ensaios = []

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(1, 4):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(4, 7):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)    
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(7, 10):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(10, 13):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(13, 16):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(16, 19):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(19, 22):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(22, 25):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(25, 28):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(i)

# popatual = criarpop(tamanhopop, tamanhoindividuo)
# for i in range(28, 31):
#     individuomaisapto = main(geracao, popatual, taxadecruzamento, taxamutacao)[1]
#     vetor_ensaios.append(individuomaisapto)
#     print(individuomaisapto)
#     print(i)
# individuomaisapto = main(geracao,popatual,taxadecruzamento,taxamutacao)[1]
# individuomenosapto = main(geracao,popatual,taxadecruzamento,taxamutacao)[2]
# aux0 = vetor_ensaios[0]
# aux1 = vetor_ensaios[1]
# aux2 = vetor_ensaios[2]
# aux3 = vetor_ensaios[3]
# aux4 = vetor_ensaios[4]
# aux5 = vetor_ensaios[5]
# aux6 = vetor_ensaios[6]
# aux7 = vetor_ensaios[7]
# aux8 = vetor_ensaios[8]
# aux9 = vetor_ensaios[9]
# aux10 = vetor_ensaios[10]
# aux11 = vetor_ensaios[11]
# aux12 = vetor_ensaios[12]
# aux13 = vetor_ensaios[13]
# aux14 = vetor_ensaios[14]
# aux15 = vetor_ensaios[15]
# aux16 = vetor_ensaios[16]
# aux17 = vetor_ensaios[17]
# aux18 = vetor_ensaios[18]
# aux19 = vetor_ensaios[19]
# aux20 = vetor_ensaios[20]
# aux21 = vetor_ensaios[21]
# aux22 = vetor_ensaios[22]
# aux23 = vetor_ensaios[23]
# aux24 = vetor_ensaios[24]
# aux25 = vetor_ensaios[25]
# aux26 = vetor_ensaios[26]
# aux27 = vetor_ensaios[27]
# aux28 = vetor_ensaios[28]
# aux29 = vetor_ensaios[29]

# media = media(aux0, aux1, aux2, aux3, aux4, aux5, aux6, aux7, aux8, aux9, aux10, aux11, aux12, aux13, aux14, aux15,
#               aux16, aux17, aux18, aux19, aux20, aux21, aux22, aux23, aux24, aux25, aux26, aux27, aux28, aux29)


fig =  plt.figure()
# x = np.linspace(0, 100, 20)
graf1 = fig.add_subplot(1,1,1)
graf1.plot(individuomaisapto,'b-')
# graf1.plot(individuomaisapto, 'r-')
# graf1.plot(individuomenosapto, 'g-')
plt.title('Média dos Melhores Individuos',fontsize ='medium')
plt.ylabel(u'Melhor individuo')
plt.xlabel(u'Gerações')
plt.grid(True)
plt.show()