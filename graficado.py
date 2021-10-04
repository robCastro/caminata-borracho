from borracho import Borracho
from bokeh.plotting import figure, show

def graficar(borracho: Borracho):
    """Genera un gráfico con todas las coordenadas por las cuales pasó el borracho"""
    fig = figure()
    # Obteniendo una lista de las posiciones x, ej: [(3, 1), (2, 1)] -> [3, 2]
    posiciones_x = list(map(lambda coordenada: coordenada[0], borracho.coordenadas))
    # Obteniendo una lista de las posiciones y, ej: [(3, 1), (2, 1)] -> [1, 1]
    posiciones_y = list(map(lambda coordenada: coordenada[1], borracho.coordenadas))
    # Generando lineas
    fig.line(posiciones_x, posiciones_y)
    # Mostrando
    show(fig)