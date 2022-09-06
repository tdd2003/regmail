import os,time,sys
try: 
    import random,re
    from random import randint
except:
    os.system("pip install faker")
import random,re
from random import randint

faker=Faker()
kytu = ['','_','.']
soluong = int(input("Nhap so luong: "))
luu = input("ten file: ")
domain = input("ten domain: ")
n = 0 
for fake in range(soluong):
    n+= 1
    num = randint(10,200)
    first_name = faker.first_name().lower()
    last_name = faker.last_name().lower()
    getkytu = random.choice(kytu)
    facemail = first_name + last_name + str(num) +"@" + domain
    print(" " " " +facemail)
    open(luu,"a").write(facemail+"\n")
