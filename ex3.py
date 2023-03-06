
# alínea a)
def bubbleSort(array):
    # loop para aceder a cada elemento do array
    for i in range(len(array)):

        # loop para comprar os elementos dentro do array
        for j in range(0, len(array) - i - 1):

            # Comparar 2 valores adjacentes no array
            #  usar > ou < para fazer sort na ordem pretendida (acendentee ou descendente)
            if array[j] > array[j + 1]:
                # alterar os elementos dentro do array se nao tiverem na ordem certa
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def bubleSortOptimized(array):
    changed=False
    for x in range(len(array)-1):
        for y in range(0,len(array)-x-1):
            if array[y]>array[y+1]:
                changed=True
                array[y],array[y+1]=array[y+1],array[y]
        if not changed:
            return
    print(array)