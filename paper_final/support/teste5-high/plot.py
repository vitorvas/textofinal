#!/usr/bin/python

import matplotlib.pyplot as plt

f = open("keffs.txt", "r")
data = f.read()
data = data.split('\n')
data = data[:-1]

print(data)

df = [float(x) for x in data]

print(df)

fig = plt.figure()
plt.grid(True)

x = fig.add_subplot(111)

x.set_title("$K_{eff}$ coupled simulation")
x.set_xlabel('Iterations')
x.set_ylabel('$K_{eff}$"')

x.plot(df, marker='o', linestyle='--', color='r')


plt.show()
        
