import numpy as np
import matplotlib.pyplot as plt
import pylab

name = str("Київ! Це те велике місто, куди він їде учитись і жити. Це те нове, що він мусить у нього ввійти, щоб осягнути свою здавна викохувану мрію. Невже Київ справді близько?")
def count_sign():
    symbols=[",", '?', '!', '.', ]
    for i in range(0, len(symbols)):
        xdata=[symbols[i]]
        ydata=[name.count(symbols[i])]
        pylab.bar(xdata, ydata)

    pylab.show()
count_sign()