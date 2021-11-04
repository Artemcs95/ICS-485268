f=open("book.txt", "r")

symbols=0
with open("book.txt") as file:
    for line in file:
        wordslist = line.split()
        wordslist2=str(wordslist)
        wordslist2.replace(' ','')
        wordslist3=list(wordslist2)
        symbols = symbols + len(wordslist3)
print("symbols without space:",symbols)