
poema=' Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo/ Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvezprecise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais éque ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixatriste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo'

versesSplit = poema.split('/')

slash = "/"

# a) Imprima na consola os 5º e 6º versos do poema.
def a():
    print("\n a) Imprima na consola os 5º e 6º versos do poema: \n")
    print(versesSplit[4] + "\n" + versesSplit[5])
    print("________________________________________________________________")

# b) Imprima na consola o poema formatado da seguinte forma:
#poema_2=' Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente'

result=""

def b():
    print("b) Imprima na consola o poema formatado da seguinte forma: \n")
    global result
    #for i in range(len(slash)):
    result = poema.replace(slash, "\n")
    print(result)
    print("________________________________________________________________")

# c) Junte a estrofe seguinte ao final do poema:
'''
Por isso eu fiz um samba bem pra frente
Dizendo realmente o que é que eu acho
Isso me deixa triste e cabisbaixo
'''

poema_3=' Por isso eu fiz um samba bem pra frente \n Dizendo realmente o que é que eu acho \n Isso me deixa triste e cabisbaixo'
novo_poema=""
def c():
    print("c) Junte a estrofe seguinte ao final do poema: \n")
    global novo_poema
    novo_poema= result+ "\n"+ poema_3
    print(novo_poema)
    print("________________________________________________________________")

# d) Imprima na consola os dois últimos versos do poema na sua forma depois das alíneas 1, 2 e 3.

poema_5=""
def d():
    global novo_poema
    global poema_5
    poema_5 = novo_poema.split("\n")
    print("d) Imprima na consola os dois últimos versos do poema na sua forma depois das alíneas 1, 2 e 3. \n")
    print(poema_5[-2]+"\n"+poema_5[-1])
    print("________________________________________________________________")


