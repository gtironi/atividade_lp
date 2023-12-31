import numpy as np
import numpy.random as npr

def gera_ndarray(num_elementos):
    a1D = npr.randint(1, 20, num_elementos)
    return a1D

#Questão 1
#Gere dois ndarrays de inteiros de uma dimensão utilizando o método de sua preferência da biblioteca NumPy
#Atribua a um terceiro ndarray a soma elemento a elemento dos dois primeiros ndarrays

def questao_1():
    arr_1 = gera_ndarray(10)
    arr_2 = gera_ndarray(10)
    arr_soma = arr_1 + arr_2
    return arr_soma

#Questão 2
# Redimensione o terceiro ndarray para duas dimensões
# Converta os dados para algum tipo de ponto flutuante
# Atribua ao terceiro ndarray sua transposta

def questao_2(arr_soma):
    arr_3 = arr_soma.reshape(2,5)
    a2D_float_c = arr_3.astype('float64') 
    print(a2D_float_c)
    a5D_float_c = np.transpose (a2D_float_c)
    print(a5D_float_c)
    return arr_3
#Questão 3
# Gere um quarto ndarray de duas dimensões utilizando o método de sua preferência da biblioteca NumPy
# Atribua ao quarto ndarray o resultado da multiplicação do quarto ndarray pelo terceiro ndarray

def questao_3(arr_3):
    arr_4 = gera_ndarray(10).reshape(2,5)
    arr_4 = arr_4 * arr_3
    return arr_4

#Questão 4
# Gere um quinto ndarray de inteiros aleatórios de uma dimensão utilizando o método de sua preferência da biblioteca NumPy Random
# Gere um sexto ndarray de inteiros aleatórios de uma dimensão utilizando o método de sua preferência da biblioteca NumPy Random
# Imprima no console todos os elementos comuns do quinto e do sexto ndarrays
# Imprima no console os índices de todos os elementos comuns do quinto e do sexto ndarrays
# Imprima no console todos os elementos do quinto ndarray que não são elementos do sexto ndarray

def questao_4():
    arr_5 = gera_ndarray(20)
    arr_6 = gera_ndarray(20)

    # Obs: Como o método usado para gerar os arrays foi o randint do numpy.random, é possível que haja duplicatas nos índices por um número se repitir.

    in_comun_number  = []

    for number in arr_5:
        if number in arr_6:
            in_comun_number.append(number)
            i_1 = np.where(arr_5 == number)
            i_2 = np.where(arr_6 == number)

            print("Número em comum:", number, f"\nÍndices no array 5 e 6 respectivamente: {i_1[0]} e {i_2[0]}")

    not_in_comun_number = []

    for number_2 in arr_5:
        if number_2 not in in_comun_number:
            not_in_comun_number.append(number_2)

    print("\nElementos do quinto array que não estão no sexto:", end = " ")
    for number_not_comun in not_in_comun_number:
        print(number_not_comun, end = " ")

    return arr_5, arr_6,

#Questão 5
# Declare um sétimo ndarray e atribua o empilhamento horizontal do quinto e do sexto ndarrays
# Imprima no console a média, desvio padrão e variância dos elementos
# A cada elemento ímpar atribua -1
# A cada elemento par atribua 1

def questao_5(arr_5, arr_6):
    arr_7 = gera_ndarray(20)
    arr_horizont = np.hstack((arr_5, arr_6, arr_7))
    
    print('Median: ', np.median(arr_horizont))
    print('Standard Deviation: ', np.std(arr_horizont))
    print('Variance: ', np.var(arr_horizont) ,'\n')
    
    arr_impares_pares = arr_horizont.copy()
    
    for i in range(len(arr_impares_pares)):
        if i%2 != 0:
            arr_impares_pares[i] = -1
        else:
            arr_impares_pares[i] = 1
            
    return arr_impares_pares

#Questão 6
# Defina dois vetores, A e B
# Imprima no console o produto vetorial AxB

def questao_6():
    vec_a = gera_ndarray(12)
    vec_b = gera_ndarray(12)

    vec_a_b =  np.dot(vec_a, vec_b)

    print(vec_a_b)

    return vec_a_b
    
#Questão 6
# Gere um oitavo ndarray de duas dimensões [3x3]
# Gere a matriz identidade
# Calcule o determinante
# Calcule a inversa e demonstre a corretude

def questao_7():
    arr_8 = np.array([[6, 1, 1], 
                  [4, -2, 5], 
                  [2, 8, 7]]) 
    identidade_3 = np.identity(3)
    determinante = np.linalg.det(arr_8)
    inversa = np.linalg.inv(arr_8)
    print("Oitavo array:\n ", arr_8)
    print("Determinante: ", determinante)
    print("Inversa:\n ", inversa)
    print("Mostrando a corretude(Oitavo array multiplicado pela inversa = identidade):\n",np.dot(arr_8, inversa).astype(int))
