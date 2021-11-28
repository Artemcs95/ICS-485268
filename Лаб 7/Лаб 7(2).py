import numpy as np
import matplotlib.pyplot as plt
import pylab


text = str("Під однією горою, коло зеленої левади, в глибокій западині стояла чимала хата Омелька Кайдаша. Хата оптонула в старому садку.")

def count_letters():
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'є', 'з', 'и', 'і','ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'х', 'ч', 'ш', 'ь', 'ю','я',]

    for i in range(0, len(alphabet)):
        xdata = [alphabet[i]]
        ydata = [text.count(alphabet[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_letters()