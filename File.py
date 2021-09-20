start="y"
while start == "y" :
    age = int(input("Скільки вам років?: "))
    todayyear = int(input("Який зараз рік?: "))
    print("Ваш рік народження: ", todayyear - age)
    start = input("Натисніть 'y' щоб продовжити або іншу клавішу щоб вийти: ")

