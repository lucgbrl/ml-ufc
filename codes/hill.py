import numpy as numpy 
import matplotlib.pyplot as plot 
from mpl_toolkits import mplot3d 

class pontos:
    def __init__(self):
        self.ponto_x = x 
        self.ponto_y = y 
        self.value = numpy.abs(self.ponto_x * numpy.sin(self.ponto_y * (numpy.pi / 4)) + self.ponto_x * sin(self.ponto_x * (numpy.pi / 4)))


def main():
    max_local, trajetoria = [], [] #inicia matrizes que irão armazenar os pontos

    while True:
        busca = int(input('Informe a quantidade de buscas a serem realizadas:'))
        if not busca <= 0:
            busca = 1
            break 
    
    #caso não seja informado um valor será realizada uma busca

    print('Máximos locais')
    for i in range(1, busca + 1):
        x_ini = round(numpy.random.uniform(-20, 20), 2)
        y_ini = round(numpy.random.uniform(-20, 20), 2)
        pontos_ini = pontos(x_ini, y_ini) #instanciando um novo ponto


        while True:
            trajetoria.append([i, round(pontos_ini.ponto_x, 2), round(pontos_ini.ponto_y, 2), round(pontos_ini.value, 6)])
            # os vizinho de pontos_ini são os pontos que variam de -0.1 a 0.1 em x e y
            vizinhos = [
                pontos(pontos_ini.ponto_x-0.01, pontos.ponto_y),
                pontos(pontos_ini.ponto_x+0.01, pontos.ponto_y),
                pontos(pontos_ini.ponto_x, pontos.ponto_y-0.01),
                pontos(pontos_ini.ponto_x, pontos.ponto_y+0.01)
            ]
            #cria um array com os valores obtidos em cada um dos vizinhos
            #cada vizinho está em um ponto proximo em 0.1 do ponto(pontos_x, pontos_y)
            valores = [ 
               v.value for v in vizinhos 
            ]

            #encontra o valor maximo no vetor de valores da vizinhança
            valor_maximo = max(valores)
            if not any((ax <= -20 or ax >= 20) for ax in [pontos_ini.ponto_x, pontos_ini.ponto_y]):
                if pontos_ini.value < valor_maximo:
                    for vizinho in vizinhos:
                        if vizinho.value == valor_maximo:
                            pontos_ini = vizinho 
                else:
                    counter = 0
                    for trajeto in trajetoria:
                        if trajeto[0] == i:
                            counter += 1 
                    max_local.append([i, pontos_ini.ponto_x, pontos_ini.ponto_y, pontos_ini.value])
                    print("A busca de numero {}: x:{} y:{} z:{} / passos: {}".format(i, round(pontos_ini.ponto_x, 2), round(pontos_ini.ponto_y, 2), round(pontos_ini.value, 6), count ))
                    break 
            else:
                print("A busca {} encontrou o limite estabelecido (-20 < x, y < 20)".format(i))
            
            maximo_global = max(max_local[i][3] for i in range(0, len(max_local)))
if __name__ == "__main__":
    main()