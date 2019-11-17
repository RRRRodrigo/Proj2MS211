# Defina as 4 constantes e as condições iniciais de u1 e u2
# Defina o tempo total e o tamanho dos intervalos de tempo
# Monte a equação (neste caso, é preferível utilizar uma biblioteca com classes e funções feitas pra esse propósito)
# Crie um vetor contendo de tamanho N, sendo N o número de passos que você deseja obter (N = tempo total/tamanho dos intervalos)
# Crie um vetor x com todos os intervalos que o gráfico precisa ter
# Crie um vetor y para armazenar os resultados de cada ponto, com y[0] = y0
# Em N vezes, calcule y[n+1] = yn + h * f(xn, yn), sendo h o tamanho do passo

import numpy as np
import matplotlib.pyplot as plt

x0 = 0
u10 = 2.7
u20 = 1.2
xf = 365
n = 3650
deltax = xf/n
c1 = 0.3
c2 = 0.15
d1 = 0.3
d2 = 0.15

x = np.linspace(x0,xf,n)

u1 = np.zeros([n])
u2 = np.zeros([n])

u1[0] = u10
u2[0] = u20

for i in range(1,n):
    j = i - 1
    func_res1 = c1*u1[i-1] - d1*u1[i-1]*u2[i-1]
    func_res2 = c2*u1[i-1]*u2[i-1] - d2*u2[i-1]
    u1[i] = deltax * (func_res1) + u1[i-1]
    u2[i] = deltax * (func_res2) + u2[i-1]

plt.plot(x,u1,'o')
plt.plot(x,u2,'o')
plt.xlabel("Valor de x")
plt.ylabel("Valor de y")
plt.title("Solucao aproximada com o metodo de Euler explicito")
plt.show()
