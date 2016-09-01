#!/usr/bin/env python3

import matplotlib.pyplot as plt

f = open('keffs.txt','r')
a = f.read()

data = [float(x) for x in a.split()]

#plt.plot(data, 'rD')
plt.plot(data, marker='o', linestyle='--', color='r', label='Square')
plt.title('$K_{eff}$ before convergence')

axes = plt.gca()

#axes.set_xlim([xmin,xmax])
axes.set_ylim([1.162,1.165])
axes.set_ylabel('$K_{eff}$')

# Evitar que mostre exponenciais
axes.get_yaxis().get_major_formatter().set_useOffset(False)

# Set x para os intervalos de time step
axes.set_xlabel('Coupled calculation iteration')

plt.grid()
plt.savefig('keffs.png')

plt.show()


