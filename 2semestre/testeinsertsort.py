import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

tamanho = 1000
lista_original = [random.randint(0, 10000) for _ in range(tamanho)]

lista_bubble = lista_original.copy()
inicio_bubble = time.time()
bubble_sort(lista_bubble)
fim_bubble = time.time()
tempo_bubble = fim_bubble - inicio_bubble

lista_insertion = lista_original.copy()
inicio_insertion = time.time()
insertion_sort(lista_insertion)
fim_insertion = time.time()
tempo_insertion = fim_insertion - inicio_insertion

print(f"Tempo de execução Bubble Sort: {tempo_bubble:.6f} segundos")
print(f"Tempo de execução Insertion Sort: {tempo_insertion:.6f} segundos")
