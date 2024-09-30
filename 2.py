import os
import sys
import json
os.system("cls")

f = open("Talabalar.json","w+")
f1 = open("Saralanganlar.json","w+")
n = int(input("Talaba soni: "))
talabalar = []
talaba = {}
sara = []
for i in range(n):
    print(f"{i+1}-Talaba")
    talaba['ism'] = input("ism: ")
    talaba['yosh'] = int(input("yosh: "))
    talaba['kurs'] = int(input("kurs: "))
    talaba['unv'] = input("unv: ")
    talabalar.append(talaba)
n = json.dumps(talabalar, indent=4)
f.write(n)
s = ''
f = open("Talabalar.json","r")
s = json.load()

f.close()
f1.close()