class Library:
 def __init__(self, name, genre, year, author):
  self.name = name
  self.grade = genre
  self.year = year
  self.author = author


book1 = ("Мартин Боруля", "пьеса", "1886", "Іван Карпенко-Карий")
book2 = ("Місто", "урбаністичний роман", "1928", "Валер'ян Підмогильний")
book3 = ("Захар Беркут", "повість", "1883", "Іван Франко")

print("Домашня бібліотека")

while True:
 print("1. Бібліотека.\n2. Пошук.\n3. Додати книгу.\n4. Видалити книгу.\n5. Вихід.\n")
 userInput = str(input())

 if userInput == "1":
  print(book1)
  print(book2)

 elif userInput == "2":
  while True:
   choice = input("Пошук книги за допомогою...\n1. name.\n2. genrе.\n3. year.\n4. author.\n")
   if choice == "1":
    while True:
     choice = input("Уведіть дані для пошуку.\n")
     if choice == 'Мартин Боруля':
      print("Пьеса,1886,Іван Карпенко-Карий")
     else:
      print("Уведіть дані для пошуку.")
      if choice == "Місто":
       print("урбаністичний роман,1928,Валер'ян Підмогильний")
      elif choice == "Захар Беркут":
       print("повість,1883,Іван Франко")
   if choice == "2":
    while True:
     choice = input("ВВедіть дані для пошуку.\n")
     if choice == "пьеса":
      print("Мартин Боруля, 1886, Іван Карпенко-Карий")
     else:
      print("Уведіть дані для пошуку.")
      if choice == "урбаністичний роман":
       print("Місто,1928,Валер'ян Підмогильний")
      elif choice == "повість":
       print("Захар Беркут,1883,Іван Франко")
   if choice == "3":
    while True:
     choice = input("Уведіть дані для пошуку.\n")
     if choice == "1886":
      print("Мартин Боруля,пьеса,Іван Карпенко-Карий")
     else:
      print("Уведіть дані для пошуку")
      if choice == "1928":
       print("Місто,урбаністичний роман,Валер'ян Підмогильний")
      elif choice == "1883":
       print("Захар Беркут,повість,Іван Франко")
   if choice == "4":
    while True:
     choice = input("ВВедіть дані для пошуку.\n")
     if choice == "Іван Карпенко-Карий":
      print("Мартин Боруля,пьеса,1886")
     else:
      print("ВВедіть дані для пошуку.")
      if choice == "Валер'ян Підмогильний":
       print("Місто,урбаністичний роман,1928")
      elif choice == "Іван Франко":
       print("Захар Беркут,повість,1883")

 elif userInput == "3":
  print("Додайте книгу.")
  filename = input()
  print("Операція успішна.")
 elif userInput == "4":
  import os

  os.remove(" D:\\booktext.txt")
 elif userInput == "5":
  break