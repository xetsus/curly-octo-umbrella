import time
nombre=input("Como te llamas?: ")
palabra="Rufo"
adivina=""
vidas=5

print("Hola: "+nombre, " Es hora de jugar al ahorcado")
print("")
time.sleep(1)
print("Comienza a adivinar")
time.sleep(0.5)
while vidas >0:
    fallas=0
    for letra in palabra:
        if letra in adivina:
            print(letra,end="")
        else:
            print("-",end="")
            fallas+=1
        
