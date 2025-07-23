import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0,50,1000)

x_loco = 676 + 8.06 * t

a_min = 0.947
x_trem_evitado = 44.72*t-0.5 *a_min *t**2
x_trem_evitado[t>47.2] = 1056

a_colisao = 0.94
x_trem_colisao = 44.72 *t -0.5*a_colisao *t**2

plt.plot(t, x_loco, label="locomotiva")
plt.plot(t, x_trem_evitado, '--', label="trem1")
plt.plot(t, x_trem_colisao, ":", label='trenm2')
plt.xlabel('tempo')
plt.ylabel('posicao')
plt.legend()
plt.show()