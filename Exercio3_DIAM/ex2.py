'''
Considere novamente o início do poema “Corrente” de Chico Buarque.
a) Escreva e execute um programa que:
1) conta o número de vogais existentes no texto;
2) imprime na consola as ocorrências da cada vogal;
3) identifica a vogal mais utilizada;
4) imprime na consola a vogal mais utilizada;
5) se existirem várias vogais empatadas com o maior número de ocorrências, deve imprimir
“Há vários vencedores.”

'''

poema='Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo/ Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Sómesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvezprecise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais éque ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixatriste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo'

vogais=['a','e','i','o','u']
slash="/"
def a1():
    counter=0
    for i in poema: # percorre caracter a caracter
        for v in vogais:
            if i==v:
                counter=counter +1
    print("a) Escreva e execute um programa que: \n")
    print("Nº de vogais existentes no poema: ", counter)
    print("________________________________________________________________")

lista=[0,0,0,0,0]
def a2():
    global lista
     # lista que vai guardar as ocorrências de cada cogal
    counter = 0
    for i in poema:  # percorre caracter a caracter
        for v in vogais:
            if i == v:
                counter = counter + 1
                if v=='a' or v=='A':
                    lista[0] +=1
                if v=='e' or v=='E':
                    lista[1] += 1
                if v == 'i' or v=='I':
                    lista[2] += 1
                if v == 'o' or v=='O':
                    lista[3] += 1
                if v == 'u' or v=='U':
                    lista[4] += 1

    print(" b) Ocorrências das vogais: \n")
    print("A: ",lista[0])
    print("E: ",lista[1])
    print("I: ",lista[2])
    print("O: ",lista[3])
    print("U: ",lista[4])
    print("________________________________________________________________")

    # podia ter feito string.count(vogal) e retorna o nº de ocorrências da vogal

def a3():
    aux=[96,126,43,87,40]
    n=['a','e','i','o','u']
    x=[aux,n]
    result=0
    k=0
    max=0
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
            k=i
            #print("i = ",lista[i])
    for j in range(len(aux)):
        if max==aux[j]:
            result=x[1][k]
    print("c) e d) Vogal mais utilizada: ", result)
    print("________________________________________________________________")

# Empate

def empate_maior(*args):
    highest = max(args)
    return args.count(highest) > 1

def print_empate(*args):
    if(empate_maior(*args)):
        print("Há vários vencedores")
        var1 = {"a": lista[0], "e": lista[1], "i": lista[2], "o": lista[3], "u": lista[4]}
        max_score = max(var1.values())
        highest_vowels= [vowel for vowel, count in var1.items() if count == max_score]
        print(highest_vowels)
    else:
        print("Não há vários vencedores")


