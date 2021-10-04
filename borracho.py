import random


class Borracho:


    __OPCIONES = (
        (0, -1), # Avanza hacia abajo
        (0, 1), # Avanza hacia arriba
        (1, 0), # Avanza a la derecha
        (-1, 0), # Avanza a la izquierda
    )


    def __init__(self, nombre: str, posicion_inicial=(0, 0)) -> None:
        """Establece a un borracho en la posicion indicada, por defecto (0, 0)"""
        self.nombre = nombre
        self._cordenadas = []
        self._cordenadas.append(posicion_inicial)


    def caminar(self) -> None:
        """Desplaza al borracho en "+/- x" o "+/- y" dentro un plano cartesiano"""
        paso_x, paso_y = random.choice(self.__OPCIONES)
        actual_x, actual_y = self._cordenadas[-1]
        nuevo_x = actual_x + paso_x
        nuevo_y = actual_y + paso_y
        self._cordenadas.append((nuevo_x, nuevo_y))


    @property
    def coordenadas(self) -> list:
        """Todas las coordenadas por las que se desplazó el borracho"""
        return self._cordenadas


    @property
    def distancia_recorrida(self) -> float:
        """Calcula la distancia entre el ultimo punto del borracho y el primero"""
        # Posicion inicial
        primer_x, primer_y = self._cordenadas[0]
        # Posicion más reciente
        ultimo_x, ultimo_y = self._cordenadas[-1]
        # Pitagoras
        distancia = ((primer_x + ultimo_x)**2 + (primer_y + ultimo_y)**2)**0.5
        return distancia