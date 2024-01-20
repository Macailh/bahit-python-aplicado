import multiprocessing

def tarea_proceso(numero):
    resultado = numero * numero
    return f"El cuadrado de {numero} es {resultado}"

if __name__ == "__main__":
    num_procesos = 4
    pool = multiprocessing.Pool(processes=num_procesos)

    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    resultados = pool.map(tarea_proceso, numeros)

    pool.close()
    pool.join()

    for resultado in resultados:
        print(resultado)
