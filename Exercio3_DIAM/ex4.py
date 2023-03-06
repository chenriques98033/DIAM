from itertools import permutations
'''
Regras:
> palavras com o mesmo número de caracteres
> letras minúsculas
> receber 2 strings e ver se são transponíveis:
    se forem transponíveis devolve true
    caso contrário, devolve false

a) Verifique se cada caracter da primeira string existe também na segunda string. Se existir, retire
o caracter na segunda string e substitua-o por “None”. Se no final do processo a segunda string
for composta apenas por “None”, então as strings podem ser transpostas. Conte o número de
passos necessários até obter a solução. Considere que um passo é uma iteração numa cadeia
de caracteres. Conte também o tempo necessário até obter a solução.


'''
import timeit


def a1(s1, s2): #amor #roma
    start = timeit.default_timer()
    steps_counter=1
    counter_S2=0
    if len(s1)!=len(s2):
        print("As strings não têm o mesmo comprimento ")
        print("Nº passos:", steps_counter)
        end = timeit.default_timer()
        print("Tempo de execução: ", end-start)
        print("___________________________________________________________________")
        return
    else:
        for i in range(len(s1)):
            steps_counter+=1
            for j in range(len(s2)):
                steps_counter+=1 # for
                steps_counter += 1 # if
                if s1[i] == s2[j]:
                    s2[j] = ""
                    steps_counter+=1
                    counter_S2 += 1

        steps_counter+=1 #if
        if counter_S2 ==len(s2):
            print("As Strings são transponíveis")
        else:
            print("As strings não saão transponíveis")
        end = timeit.default_timer()
        print("Tempo que demora a correr o programa: ", end-start)
        print("Nº passos:", steps_counter)
        print("________________________________________________________________")

def a2(s1,s2):
    res1 = "".join(sorted(s1))
    res2 = "".join(sorted(s2))
    #s1.sort()
    #s2.sort()
    print("s1=",res1)
    print("s2=",res2)
    start = timeit.default_timer()
    steps_counter = 2
    if len(s1) != len(s2):
        print("As strings não têm o mesmo comprimento ")
        print("Nº passos:", steps_counter)
        return
    else:
        steps_counter += 1
        if res1 == res2:
            print("As palavras são iguais, então são transponíveis")
            print("Nº passos:", steps_counter)



    print("________________________________________________________________")

def combinations(str):
    result = set()
    for i in range(1, len(str) + 1):
        result.update("".join(r) for r in permutations(str, i))
    return result

def forca_bruta(str1,str2):
    steps_Counter=1 + len(str2)
    start = timeit.default_timer()
    if str2 in combinations(str1):
        end = timeit.default_timer()
        print(" Tempo de exceucção: ", end - start)
        print(" Nº de passos", steps_Counter)
        print("--------------------------------------------------------")
        return True
    end = timeit.default_timer()
    print(" Tempo de exceucção: ",end-start)
    print(" Nº de passos", steps_Counter)
    print("--------------------------------------------------------")
    return False


def d(s1,s2):
    start = timeit.default_timer()
    d={}
    d_2={}
    steps_Counter = 2
    for i in s1:
        d[i]= s1.count(i)
        steps_Counter += 1

    for j in s2:
        d_2[j]=s2.count(j)
        steps_Counter += 1

    booleano=False
    for k,v in d.items():
        steps_Counter += len(d.items())
        for key,value in d_2.items():
            steps_Counter += len(d_2.items())
            steps_Counter+=1
            if k==key and v==value:
                booleano=False
            else:
                booleano=True

    print("dicionário 1 k,v",d.items())
    print("dicionário 2 k,v", d_2.items())
    steps_Counter += 1
    if booleano == True:
        end= timeit.default_timer()
        print("As palavras são transponíveis")
        print(" Tempo de exceucção: ", end - start)
        print("Nº de passos: ",steps_Counter)
    else:
        end = timeit.default_timer()
        print("As palavras não são transponíveis")
        print(" Tempo de exceucção: ", end - start)
        print("Nº de passos: ", steps_Counter)

    print("--------------------------------------------------------")




