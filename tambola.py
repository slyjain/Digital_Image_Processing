
import random
import numpy as np
tambola = np.zeros((3, 9))

def createTambolaRow(n):
    count = 0
    hashArray = [0] * n
    while count < 5:
        random_int = random.randint(0, 8)  
        if hashArray[random_int] == 0:
            hashArray[random_int] = 1
            count += 1
    return hashArray
for i in range(3):
  tambola[i]=createTambolaRow(9)
  
def hashArrayGenerator():
    all_hash_arrays = []
    for i in range(9):
        hashArray = [0] * 10
        count = 0
        while count < 3:
            random_int = random.randint(0, 9)  
            if hashArray[random_int] == 0:
                hashArray[random_int] = 1
                count += 1
        all_hash_arrays.append(hashArray)
    return all_hash_arrays

hashArray=hashArrayGenerator()
def createTambola(hashArray):
   
    for i in range(9):
      k=0
      for j in range(10):
          if hashArray[i][j]==1:
            tambola[k][i]=(i*10+j+1)*tambola[k][i]
            k+=1
    return tambola        
tambola=createTambola(hashArray)

print(tambola)
for i in range(3):
    for j in range(9):
        if tambola[i][j]!=0:
            print("|",tambola[i][j],end="")
        else:
            print("| |",end="")
    print()

