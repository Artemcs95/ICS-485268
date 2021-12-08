import matplotlib.pyplot as plt

beef = [25.88, 24.00, 25.25]
pork = [25.43,26.08,26.95]
salo = [14.48,14.73,15.65]
year = ['2013', '2014', '2015']

plt.plot(year,beef,label = "Яловичина")
plt.plot(year,pork,label = "Свинина")
plt.plot(year,salo,label = "Сало")
plt.xlabel("Рік")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def graph():
    plt.show()