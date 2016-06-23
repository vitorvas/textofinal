#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

# Read data from matlab like files
# Command used to save the file in octave
# (save -6 myfile.mat B1_DIFFCOEF B1_TOT B1_NSF B1_S0)

octave_data = sio.loadmat('myfileconv.mat')
b1d = octave_data['B1_DIFFCOEF']
b1tot = octave_data['B1_TOT']
b1nsf = octave_data['B1_NSF']
b1s0 = octave_data['B1_S0']

# A ideia é gerar duas figuras diferentes
# Cada uma com 4 gráficos.
# Cada gráfico para cada coeficiente nas 4 temperaturas
# mostrando os 3 materiais

# Temperaturas de cada material
xfuel = np.array([300,400,500,600])
xcladding = np.array([300, 396, 403, 410])
xcoolant = np.array([300, 308.5, 317, 341])

# Primeiro teste para o b1s0iffcoef
b1s0_mat1_g1 = b1s0[0:12:3,0]
b1s0_mat1_g1_error = b1s0[0:12:3,1]

b1s0_mat1_g2 = b1s0[0:12:3,2]
b1s0_mat1_g2_error = b1s0[0:12:3,3]

b1s0_mat2_g1 = b1s0[1:12:3,0]
b1s0_mat2_g1_error = b1s0[1:12:3,1]

b1s0_mat2_g2 = b1s0[1:12:3,2]
b1s0_mat2_g2_error = b1s0[1:12:3,3]

b1s0_mat3_g1 = b1s0[2:12:3,0]
b1s0_mat3_g1_error = b1s0[2:12:3,1]

b1s0_mat3_g2 = b1s0[2:12:3,2]
b1s0_mat3_g2_error = b1s0[2:12:3,3]

# First illustrate basic pyplot interface, using defaults where possible.
fig, axs = plt.subplots(nrows=3, ncols=2, sharex=False)
fig.set_size_inches(6, 8, forward=True)


# Graphic for fuel G1 -------------------------------------------------------------------------
ax = axs[0,0]
ax.grid(True)
ax.errorbar(xfuel, b1s0_mat1_g1, b1s0_mat1_g1_error, fmt='-or')

# set axis to be 1% bigger in y and x
ax.axis([290, 610, 0.6971, 0.6986])
ax.set_xticks(np.arange(300, 700, 100))
ax.set_ylabel('barns ($\sigma$)')
ax.ticklabel_format(useOffset=False)
ax.set_title('Total XS group 1')
ax.annotate("Fuel", xy=(0.1,0.88),xycoords='axes fraction', fontsize=14)


#Graphic for cladding G1 ----------------------------------------------------------------------
ax = axs[1,0]
ax.grid(True)
ax.errorbar(xcladding, b1s0_mat2_g1, b1s0_mat2_g1_error, fmt='-og')

# set axis to be 1% bigger in y and x
ax.axis([xcladding[0]*0.99, xcladding[-1]*1.01, b1s0_mat2_g1[0]*0.99, b1s0_mat2_g1[-1]*1.01])
ax.set_xticks(np.arange(300, 450, 30))
ax.set_ylabel('barns ($\sigma$)')
ax.ticklabel_format(useOffset=False)
#ax.set_title('Total Cross Sections: cladding (group 1)')
ax.annotate("Cladding", xy=(0.1,0.85),xycoords='axes fraction', fontsize=14)

#Graphic for coolant G1------------------------------------------------------------------------
ax = axs[2,0]
ax.grid(True)
ax.errorbar(xcoolant, b1s0_mat3_g1, b1s0_mat3_g1_error, fmt='-ob')

# set axis to be 1% bigger in y and x
ax.axis([xcoolant[0]*0.99, xcoolant[-1]*1.01, 0.9532, 0.9538])
ax.set_ylabel('barns ($\sigma$)')
ax.ticklabel_format(useOffset=False)
#ax.set_title('Total Cross Sections: coolant (group 1)')
ax.annotate("Coolant", xy=(0.1,0.85),xycoords='axes fraction', fontsize=14)

ax.set_xlabel('Temperature (K)')

# Graphic for fuel G2 -------------------------------------------------------------------------
ax = axs[0,1]
ax.grid(True)
ax.errorbar(xfuel, b1s0_mat1_g2, b1s0_mat1_g2_error, fmt='-sr')

# set axis to be 1% bigger in y and x

ax.axis([290, 610, 1.965, 1.995])
ax.set_xticks(np.arange(300, 700, 100))
#ax.set_ylabel('barns ($\sigma$)')
ax.ticklabel_format(useOffset=False)
ax.set_title('Total XS group 2')
ax.annotate("Fuel", xy=(0.1,0.88),xycoords='axes fraction', fontsize=14)


#Graphic for cladding G2 ----------------------------------------------------------------------
ax = axs[1,1]
ax.grid(True)
ax.errorbar(xcladding, b1s0_mat2_g2, b1s0_mat2_g2_error, fmt='-sg')

# set axis to be 1% bigger in y and x
ax.axis([xcladding[0]*0.99, xcladding[-1]*1.01, b1s0_mat2_g2[0]*0.99, b1s0_mat2_g2[-1]*1.01])
#ax.set_ylabel('barns ($\sigma$)')
ax.set_xticks(np.arange(300, 450, 30))
ax.ticklabel_format(useOffset=False)
#ax.set_title('Total Cross Sections: cladding (group 1)')
ax.annotate("Cladding", xy=(0.1,0.85),xycoords='axes fraction', fontsize=14)


#Graphic for coolant G2 -----------------------------------------------------------------------
ax = axs[2,1]
ax.grid(True)
ax.errorbar(xcoolant, b1s0_mat3_g2, b1s0_mat3_g2_error, fmt='-sb')

# set axis to be 1% bigger in y and x
ax.axis([xcoolant[0]*0.99, xcoolant[-1]*1.01, b1s0_mat3_g2[0]*0.99, b1s0_mat3_g2[-1]*1.01])
#ax.set_ylabel('barns ($\sigma$)')
ax.ticklabel_format(useOffset=False)
#ax.set_title('Total Cross Sections: coolant (group 1)')
ax.annotate("Coolant", xy=(0.1,0.85),xycoords='axes fraction', fontsize=14)

ax.set_xlabel('Temperature (K)')

# Ajusta os eixos entre is
plt.tight_layout()

plt.savefig('errorbar_s0xs.png', dpi=300)

plt.show()



