from matplotlib import pyplot as plt
import numpy as np
from random import randint


# def selecao(vetor_avaliado, vetor_populacao):
# 	soma_aptidao = 0
# 	acumulador = 0
# 	for i in range(0,len(vetor_avaliado)):
# 		soma_aptidao += vetor_avaliado[i]
# 	selecionado = []
# 	r = uniform(0,soma_aptidao)
# 	i = 0
# 	while len(selecionado) != len(vetor_populacao):		
# 		acumulador += vetor_avaliado[i]
# 		if acumulador >= r:
# 				selecionado = vetor_populacao[i]
# 				break
# 		i += 1
# 		# for k in range(0, len(vetor_avaliado)):			
# 		# 	acumulador += vetor_avaliado[k]
# 		# 	if acumulador >= r:
# 		# 		selecionado = vetor_populacao[k]
# 		# 		selecionado.append(aux)
# 		# 		break

# 	return selecionado
# -----------------------
# def selecao(vetor_avaliado, vetor_populacao):
# 	soma_aptidao = 0
	
# 	for i in range(0,len(vetor_avaliado)):
# 		soma_aptidao += vetor_avaliado[i]
# 	selecionado = []
# 	# i = 0
# 	while len(selecionado) != len(vetor_populacao):		
# 		r = 0
# 		acumulador = 0
# 		aux = []
# 		r = uniform(0,soma_aptidao)
# 		for k in range(0, len(vetor_avaliado)):			
# 			acumulador += vetor_avaliado[k]
# 			if acumulador >= r:
# 				aux = vetor_populacao[k]
# 				selecionado.append(aux)
# 				break
				
# 	return selecionado
# import matplotlib.pyplot as plt
# a = [0.1,0.2,0.3,0.4,0.5]
# b = [1,2,3,4,5]
# plt.plot(a,b, 'y-')
# plt.ylabel(u'Número de Individuos')
# plt.xlabel(u'Chupa que é de Uva')
# plt.show()

# def teste(a,b):
# 	c = [0,1,2,3,4]
# 	d = [0,21]
# 	return (c,d)

# result = teste(4,5)[1]
# print('a')
# print('\n')
# print(result)

# import numpy as np
# import matplotlib.pyplot as plt

# # example data
# x = np.arange(0.1, 4, 0.5)
# y = np.exp(-x)
# # example error bar values that vary with x-position
# error = 0.1 + 0.2 * x
# # error bar values w/ different -/+ errors
# lower_error = 0.4 * error
# upper_error = error
# asymmetric_error = [lower_error, upper_error]

# fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
# ax0.errorbar(x, y, yerr=error, fmt='-o')
# ax0.set_title('variable, symmetric error')

# ax1.errorbar(x, y, xerr=asymmetric_error, fmt='o')
# ax1.set_title('variable, asymmetric error')
# ax1.set_yscale('log')
# plt.show()
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# indiviomaisapto = np.arange(0.0, 5.0, 0.1)
# mediaindividuomaisapto = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

# x = np.arange(0, 10, 0.1)
# print(x)

# a = []
# for i in range(0,len(x)):
# 	a.append(randint(0,1000))
# print(a)	
# plt.plot(x,a,'b-')
# plt.show()

# for i in range(0,30):
# 	if i > 5 and i <=10:
# 		print(i)
# 	if i > 10 and i <=20:
# 		print(i)
# 	if i > 20 and i <=30:
# 		print(i)


# Muito Importante
# pop_final = main(geracao,tamanhopop,tamanhoindividuo,taxadecruzamento,taxamutacao)[0]
# 	individuomaisapto = main(geracao,tamanhopop,tamanhoindividuo,taxadecruzamento,taxamutacao)[1]
# 	pop_final_int = decodint(pop_final)
# 	pop_final_real = decodreal(pop_final_int)
# 	popfinalavaliada = avalia_pop(pop_final_real)
# 	vetor_ensaios.append(individuomaisapto) 

# a =[[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,10]]

# aux1 = a[0], aux2 = a[1], aux3 = a[2]

# print(aux1)
# print(aux2)
# print(aux3)
a = (9+
4+5)
print (a)