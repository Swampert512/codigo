########LAB12######
import numpy as np

cartas = ["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]
premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

#paso 1. Cree una función llamada imprimir que imprima el tamaño de una lista de entrada y los elementos que la
#conforman. Esta función puede ser de utilidad en cada uno de los pasos posteriores para verificar los resultados.
def imprimir(lis):
    print(len(lis))
    return lis[:]

#2. Utilice la función imprimir creada para mostrar los elementos contenidos en las listas cartas y premium.
#print(imprimir(cartas))

#3. Cree una función llamada generador.
N=5
n=10
def generador(lisA, x):
    R=np.random.choice(lisA, x, replace=False)
    return R

#4. crear una variable "jugador"
jugador=generador(cartas, n)

#5. crear la variable combinador
def combinador(lisA, lisB):
    lisA.extend(lisB)
    R=np.random.choice(lisA, len(lisA), replace=False)
    return R


#6. el resultado de combinador almacenarlo en una variable llamada "juego"
juego=combinador(cartas, premium)


#7. utilizar la funcion generador para generar 5 sobres
sobre_uno=generador(juego, N)
sobre_dos=generador(juego, N)
sobre_tres=generador(juego, N)

#8 NO HALLE LA FORMA DE HACER EL PUNTO 8 CON LA FUNCION COMBINDOR, me lanzaba
#AttributeError: 'numpy.ndarray' object has no attribute 'extend' 

paquete=[]
paquete.extend(sobre_dos)
paquete.extend(sobre_uno)
paquete.extend(sobre_tres)


#9. crear una funcion llamada loteria que de un 10%de probabilidad de dar una 
#cata premium
control=[]

def loteria():
    a=range(10)
    u=np.random.choice(a, 1, replace=False)
    if u>0:
        p=0
        for i in paquete:
            c=paquete.count(i)
            control.extend(str(c))
            if i in premium:
                p+=1
        for o in control:
            if (o>="2") and p<=1:
                while True:
                    k=np.random.choice(premium, 1, replace=False)
                    if k in paquete==False:
                        paquete.extend(k)
                        return paquete
                    break
        else:
            k=np.random.choice(premium, 1, replace=False)
            paquete.extend(k)
            return paquete
    else:
        return paquete
jugador1=[]
jugador1.extend(jugador)
jugador1.extend(paquete)
####################################

#10.1
c=['Hardin', 'Blake', 'Park', 'Stanton', 'Ratliff', 'Higgins', 'Flowers', 'Terry', 'Grant', 'Robiar', 'Crane', 'Smith', 'Mooney', 'Bryan', 'Buck', 'Powers', 'Aramis', 'Hubbard', 'Lightbringer', 'Flowers', 'Houston', 'Burnett', 'Hubbard', 'Hancock', 'Deleon']
premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

C=[]
for i in c:
    if i in premium:
        C.append(i)
print(C)

#10.2
c=['Hardin', 'Blake', 'Park', 'Stanton', 'Ratliff', 'Higgins', 'Flowers', 'Terry', 'Grant', 'Robiar', 'Crane', 'Smith', 'Mooney', 'Bryan', 'Buck', 'Powers', 'Aramis', 'Hubbard', 'Lightbringer', 'Flowers', 'Houston', 'Burnett', 'Hubbard', 'Hancock', 'Deleon']
C=[]
for i in c:
    x=c.count(i)
    if x>1:
        C.append(i)
        C.append(x)
print(C)







#10.3
c=['Hardin', 'Blake', 'Park', 'Stanton', 'Ratliff', 'Higgins', 'Flowers', 'Terry', 'Grant', 'Robiar', 'Crane', 'Smith', 'Mooney', 'Bryan', 'Buck', 'Powers', 'Aramis', 'Hubbard', 'Lightbringer', 'Flowers', 'Houston', 'Burnett', 'Hubbard', 'Hancock', 'Deleon']
C=[]
for i in c:
    x=c.count(i)
    C.append(i)
    C.append(x)
print(C)







#10.4
c=['Hardin', 'Blake', 'Park', 'Stanton', 'Ratliff', 'Higgins', 'Flowers', 'Terry', 'Grant', 'Robiar', 'Crane', 'Smith', 'Mooney', 'Bryan', 'Buck', 'Powers', 'Aramis', 'Hubbard', 'Lightbringer', 'Flowers', 'Houston', 'Burnett', 'Hubbard', 'Hancock', 'Deleon']
al=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l=[i.lower for i in c]
w=[]
for i in al:
    x=0
    for o in l:
        if i in o[0]:
            x+=1
    w.append(f"con {i} hay {x} cartas")
print(w)



#10.5
c=['Hardin', 'Blake', 'Park', 'Stanton', 'Ratliff', 'Higgins', 'Flowers', 'Terry', 'Grant', 'Robiar', 'Crane', 'Smith', 'Mooney', 'Bryan', 'Buck', 'Powers', 'Aramis', 'Hubbard', 'Lightbringer', 'Flowers', 'Houston', 'Burnett', 'Hubbard', 'Hancock', 'Deleon']

l=0
t=100
letrap="rabbit"
letrag="mulan"
for i in c:
    x=len(i)
    if x>l:    #esta es la ams larga
        l=x
        letrag=i
print(f"la mas larga es {letrag} con {l} letras")

for o in c:
    p=len(o)
    if p<t: 
        t=p
        letrap=o
print(f"la mas corta es {letrap} con {t} letras")


#10.6
c=['Hardin', 'Blake', 'Park', 'Stanton', 'Ratliff', 'Higgins', 'Flowers', 'Terry', 'Grant', 'Robiar', 'Crane', 'Smith', 'Mooney', 'Bryan', 'Buck', 'Powers', 'Aramis', 'Hubbard', 'Lightbringer', 'Flowers', 'Houston', 'Burnett', 'Hubbard', 'Hancock', 'Deleon']
premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]
x=0
w=0
for i in premium:
    w+=1
    if i in c:
        for o in c:
            if i[0]==o[0]:
                x+=1
    elif w>=5:
        print("no tiene cartas con las caracteristicas especificadas")
    elif x>0:
        print(f"hay {x} cartas con esas caracteristicas")
