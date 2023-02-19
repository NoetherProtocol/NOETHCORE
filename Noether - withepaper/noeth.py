import numpy as np
import matplotlib.pyplot as plt
import math
import random


#Parameters:
# t: heat of the network.
# n: epoch -> aprox. 5 days. 

k = lambda x: x ** 2 

def kappa_map(k_n, n, t=0, alpha=100):
	return (k_n + (1 + t)*alpha / n), n + 1

# Initial
k = 10000
n = 1

# Emission per epoch loop. 
# 73 epoch -> 1 year of emission.

y = []
epoch = []
heat_of_net = np.loadtxt('adoption_model.txt')[:,1]

heat_of_net[0:73 * 2] *= 5
heat_of_net[73 * 2:73 * 4] *= 10
heat_of_net[73 * 4:73 * 6] *= 15
heat_of_net[73 * 6:73 * 8] *= 30
heat_of_net[73 * 8:73 * 10] *= 80
heat_of_net[73 * 10:73 * 30] *= (100 + random.randrange(100))
heat_of_net[73 * 30:] *= (1000 + random.randrange(100))

years = 100
halving = 1

for i in range(73*years):
	heat_t = heat_of_net[i]
	if i % (73 * halving) == 0:
		print('flag', i)
		k, n = kappa_map(k, n, heat_t)
		print(k)
		k = 0.9 * k
	else:
		k, n = kappa_map(k, n)
		print(k)
	
	y.append(k)
	epoch.append(n)


plt.xlabel('Year')
plt.ylabel('Adopters per year')
plt.plot(np.array(epoch).reshape(73 * years) / 73, heat_of_net[0: 73 * years])
plt.savefig("adopter_per_year.png")
plt.show()

# Gráficos emision y total supply. 

suma = np.array(y)
lista_suma = [suma[:i].sum() for i in range(len(epoch)) ]

plt.ylabel('NOETH emission per year')
plt.plot(np.array(epoch)/73, y)
plt.savefig("noth_emission.png")
plt.show()

plt.subplot(3, 1, 1)
plt.ylabel('Adopters per year')
plt.plot(np.array(epoch).reshape(73 * years) / 73, heat_of_net[0:73 * years])

plt.subplot(3, 1, 2)
plt.ylabel('NOETH Emission per year ')
plt.plot(np.array(epoch) / 73, y)

plt.subplot(3, 1, 3)
plt.ylabel('Total Circulation')
plt.xlabel('Year')
plt.plot(np.array([epoch]).reshape(73 * years) / 73, lista_suma)

plt.show()

plt.ylabel('Total Circulation')
plt.xlabel('Years')
plt.plot(np.array([epoch]).reshape(73 * years) / 73, lista_suma)
plt.savefig("total_circualtion.png")
plt.show()


