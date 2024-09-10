print("Mas sobre funciones")
# Aqui se escriben las funciones
def sumaab_(a,b):
    s=a+b
    return s

def resta_(c,d):
    r=c-d
    return r

def mult_(y,z):
    m=y*z
    return m

def div_(x,v):
    di=x/v
    return di

#Llamadas a funciones

print("----------Calculando suma----------------")
s1=int(input("Ingresa el primer Numero: "))
s2=int(input("Ingresa el segundo Numero: "))
suma=sumaab_(s1,s2)
print(f"La suma de {s1} + {s2} = {suma}")

print("----------Calculando resta---------------")
r1=int(input("Ingresa el primer Numero: "))
r2=int(input("Ingresa el segundo Numero: "))
resta=resta_(r1,r2)
print(f"La resta de {r1} - {r2} = {resta}")

print("----------Calculando multiplicacion------")
m1=int(input("Ingresa el primer Numero: "))
m2=int(input("Ingresa el segundo Numero: "))
mult=mult_(m1,m2)
print(f"La multiplicacion de {m1} X {m2} = {mult}")

print("----------Calculando division------------")
d1=int(input("Ingresa el primer Numero: "))
d2=int(input("Ingresa el segundo Numero: "))
div=div_(d1,d2)
print(f"La division de {d1} / {d2} = {div}")