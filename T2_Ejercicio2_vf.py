def suma_rango(lista, pi, pf):
    if pi > pf:
        return 0
    return lista[pi - 1] + suma_rango(lista, pi + 1, pf)
def main():
    n = int(input("Ingrese el tamaño del arreglo: "))
    lista = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    print("Lista:", lista)
    pi = int(input("Posición inicial desde el 1: "))
    pf = int(input("Posición final desde el 1: "))
    if pi < 0 or pf >= len(lista) or pi > pf:
        print("Error en las posiciones")
        return
    resultado = suma_rango(lista, pi, pf)
    print("Resultado:", resultado)
main()
