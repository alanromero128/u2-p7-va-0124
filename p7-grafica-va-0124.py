import numpy as np
import matplotlib.pyplot as plt

no_lista=[1,2,3,17,48]
califa_ml=[20,30,80,100,90]
califa_va=[70,90,60,90,80]
plt.plot(no_lista,califa_ml,label="Califa ML")
plt.plot(no_lista,califa_va,label="Califa VA")
plt.title("Calificaciones materias 0124")
plt.xlabel("Numero de lista")
plt.ylabel("calificacion")
plt.legend("Alan 0124")
plt.show()