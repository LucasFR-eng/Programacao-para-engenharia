def part(array,inicio,final):
    pivo = vetor[final]
    i = inicio - 1
    for j in range(inicio,final):
        if array[j] <= pivo:
            i = i + 1
            array[i],array[j] = array[j],array[i]
    array[i + 1],array[final] = array[final],array[i + 1]
    return i + 1
def quick_sort(vetor,inicio,final):
    if inicio < final:
        posicao = part(vetor,inicio,final)   
        quick_sort(vetor,inicio,posicao - 1)
        quick_sort(vetor,posicao + 1,final)

vetor = [2,9,7,4,56,45,23,46,99]
quick_sort(vetor, 0, len(vetor) - 1)
print(vetor)