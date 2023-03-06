# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ex1
import ex2
import ex3
import ex4

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(">>>>>> Exercício 3.1 <<<<<<")
    ex1.a()
    ex1.b()
    ex1.c()
    ex1.d()
#---------------------------------------------------------------------------------
    print(">>>>> Exercício 3.2 <<<<<<")
    ex2.a1()
    ex2.a2()
    ex2.a3()
    ex2.print_empate(ex2.lista[0],ex2.lista[1],ex2.lista[2],ex2.lista[3],ex2.lista[4])
#----------------------------------------------------------------------------------

#exercíio 3.3-a)
    print(">>>>> Exercício 3.3 <<<<<<")
    data = [-2, 45, 0, 11, -9]
    ex3.bubbleSort(data)
    print('Sorted na ordem acendente:')
    print(data)
    print('print bublble sort otimizado')
    ex3.bubleSortOptimized(data)


#3.3 -b)
    data_2= [-2, 45, 0, 11, -9]
    ex3.bubleSortOptimized(data_2)


#-----------------------------------------------------------------------------------
    print(">>>>> Exercício 3.4 <<<<<<")
# teste para palavras transponíveis:
    ex4.a1(['a','m','o','r'],['r','o','m','a'])

# teste para palavras n~so transponíveis:
    ex4.a1(['a', 'm', 'o', 'r'], ['r', 'o', 'c', 'k'])

# teste para palavras com diferente comprimento:
    ex4.a1(['a','m','o','r'],['a','r','r','o','z'])

#teste para verificar se deuas palavras depois de ordenadas são iguais:
#ex4.a2(['a','m','o','r'],['r','o','m','a'])
    ex4.a2("amor","roma")


# força bruta
    ex4.forca_bruta("amor","roma")

# teste para verificar se as palavras têm a mesma quantidade de letras que compõem a palavra
#ex4.d("amor","roma")
    ex4.d("amor","mora")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
