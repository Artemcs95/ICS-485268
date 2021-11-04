filename = "group.txt"
import csv
import sys
from typing import Text, Type

print("\n1. Print a string\n2. Read the file\n3. Add new content\n4. Search by keyword\n")
Type = str(input())
if Type == "1":
    print("Enter a string that you want to print")
    line1 = int(input())
    line = open(filename).readlines()[line1] 
    print("\n"+line)
    
if Type == "2":
    file = open(filename, "r")
    reader = csv.reader(file, delimiter="\t")
    print("Reading the file with name: 'group.txt'")
    for row in reader:
        print(row) 
    
if Type == "3":
    print("Enter a new text to write to 'group.txt'") 
    Text = (str(input())+"\n")
    file1 = open(filename, "a+")
    file1.write(Text)
    print("\nText is added\n")
    file1.close()
        
if Type == "4":
    print("Enter a key word to search for")
    searchInput = str(input())
    file1 = open(filename, "r")
    file2 = file1.readlines()
        
    for row in file2:
        if searchInput in row:
            print(row)