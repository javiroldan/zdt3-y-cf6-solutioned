
import matplotlib.pyplot as plt
from setuptools._vendor.packaging.tags import _mac_arch
import main as _main
import ZDT3 as ZDT3



def crea_pelicula(peli):
    res = []
    for i in range(0,_main.N):
        z = ZDT3.func(peli[i])
        plt.plot(z[0],z[1],marker="o",color="red")
    plt.show()


#if __name__ == "__main__":
