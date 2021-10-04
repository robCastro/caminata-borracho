from borracho import Borracho
from graficado import graficar


def simular(numero_pasos: int) -> float:
    """Crea un borracho, lo hace caminar las n veces indicadas por numero_pasos, y gráfica el resultado de la caminata"""
    borracho = Borracho('Roberto')
    # Caminar n veces
    for _ in range(numero_pasos): borracho.caminar()
    graficar(borracho)
    # Retornar la distancia total recorrida
    return borracho.distancia_recorrida


def main():
    """Ejecuta las simulaciones para cada elemento dentro lista de pasos a simular"""
    lista_pasos_a_simular = [10, 100, 1000, 10000, 100000]
    distancias_recorridas = []
    for numero_pasos_a_simular in lista_pasos_a_simular:
        distancia_recorrida = simular(numero_pasos_a_simular)
        distancias_recorridas.append(distancia_recorrida)
    print(lista_pasos_a_simular)
    print(distancias_recorridas)


if __name__ == "__main__":
    main()