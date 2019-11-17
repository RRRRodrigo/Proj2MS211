import numpy as np
import matplotlib.pyplot as plt

x0 = 0
u10 = 3.0
u20 = 1.0
xf = 365
n = 3650
deltax = xf/n

c1 = 0.1
c2 = 0.05
d1 = 0.1
d2 = 0.05

x = np.linspace(x0,xf,n)

u1 = np.zeros([n])
u2 = np.zeros([n])

u1[0] = u10
u2[0] = u20

for i in range(1,n):
    j = i - 1
    func_res1 = c1*u1[i-1] - d1*u1[i-1]*u2[i-1]
    K1 = deltax * func_res1
    func_res1 = c1*(u1[i-1] + K1/2) - d1*(u1[i-1] + K1/2)*(u2[i-1] + deltax/2)
    K2 = deltax * func_res1
    func_res1 = c1*(u1[i-1] + K2/2) - d1*(u1[i-1] + K2/2)*(u2[i-1] + deltax/2)
    K3 = deltax * func_res1
    func_res1 = c1*(u1[i-1] + K3) - d1*(u1[i-1] + K3)*(u2[i-1] + deltax)
    K4 = deltax * func_res1
    u1[i] = u1[i-1] + K1/6 + K2/3 + K3/3 + K4/6
    func_res2 = c2*u1[i-1]*u2[i-1] - d2*u2[i-1]
    K1 = deltax * func_res2
    func_res2 = c2*(u1[i-1] + deltax/2)*(u2[i-1] + K1/2) - d2*(u2[i-1] + K1/2)
    K2 = deltax * func_res2
    func_res2 = c2*(u1[i-1] + deltax/2)*(u2[i-1] + K2/2) - d2*(u2[i-1] + K2/2)
    K3 = deltax * func_res2
    func_res2 = c2*(u1[i-1] + deltax)*(u2[i-1] + K3) - d2*(u2[i-1] + K3)
    K4 = deltax * func_res2
    u2[i] = u2[i-1] + K1/6 + K2/3 + K3/3 + K4/6

plt.plot(x,u1,'o')
plt.plot(x,u2,'o')
plt.xlabel("Valor de x")
plt.ylabel("Valor de y")
plt.title("Solucao aproximada com o metodo de Euler explicito")
plt.show()
